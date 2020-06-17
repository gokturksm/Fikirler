import numpy as np
import pandas as pd

df = pd.DataFrame(data=5)


def complex_degree(z, deg=0):
    rad = np.deg2rad(deg)
    a: float = z * np.cos(rad)
    b: float = z * np.sin(rad)
    return a + 1j * b


def voltage(val: float, val_type: str='eff') -> float:
    if val_type is 'max':
        result = val / np.sqrt(2)
    elif val_type is 'eff':
        result = val
    else:
        result = 0.0
    return result


def complex_input(vars):
    """
    input 1 : r1+i1.j, r2+i2.j, ...
    input 2 : (z1, deg1), (z2, d2)
    """
    comp = isinstance(vars[0], tuple)

    if comp:
        vars = [complex_degree(*_) for _ in vars]

    return tuple(vars)

a = complex_degree(1, 120)


# örnek:
# dengesiz sistem fazörleri verilmiş ise

donusum_matrisi = np.array([[1, 1, 1],
                            [1, a, np.square(a)],
                            [1, np.square(a), a]])


def get_result(arr):
    z = np.absolute(arr)
    deg = np.rad2deg(np.angle(arr))
    return z, deg

# va, vb, vc dengesiz fazörleri biliniyorsa
giris = (1, 0), (1.2, -110), (0.9, 120)

complex_giris = complex_input(giris)

complex_a = np.true_divide(1, 3) * np.dot(donusum_matrisi, complex_giris)
complex_b = complex_a * donusum_matrisi[2]
complex_c = complex_a * donusum_matrisi[1]

z1, deg1 = get_result(complex_a)
z2, deg2 = get_result(complex_b)
z3, deg3 = get_result(complex_c)


