import numpy as np
import pandas as pd

pv_vals = pd.Series(np.random.random_integers(0, 10, 50), name='PV')
load_vals = pd.Series(np.random.random_integers(0, 20, 50), name='LOAD')


class house_load:
    def __init__(self):
        self.from_pv = 0
        self.from_grid, self.to_grid = 0, 0
        self.ex_times = []

    
    def usage(self, time):
        pv = pv_vals.iloc[int(time)]
        usage = load_vals.iloc[int(time)]
        ex = usage - pv

        if ex > 0:
            self.from_pv += pv
            self.from_grid += ex
        else:
            self.from_pv += usage
            self.to_grid += abs(ex)
            self.ex_times.append(time)


a = house_load()

for i in range(len(pv_vals)):
    a.usage(i)

"""
Not:
Şimdi burada ufak bir batarya olsa ve biz de öteleme için gerekli olan enerjiyi elde edene kadar enerji biriktirsek.
Ve biriktirenler de en sonunda ilgili kişiye enerjiyi satmış olacak.
Zaman kısıtına da bakarız, belirli bir miktar biriktiyse o kadarı yoksa zaten normal olacak.
Bataryasız olursa fiyat belirleme çok muğlak oluyor. Bizim durumda fiyatlama çok kolay oluyor.

Bu yöntemin bataryalı sistemle farkı nedir?
Bu sistemde batarya boyutu yüksek değil, apartmandaki ötelenebilir yüklerin belirli miktarı aynı anda çalışacak
diye ele alınabilir. Bu da batarya kapasitesi olabilir. Batarya öncelikle sadece doldurulacak.
Dolduranlar bataryaya enerji satmış olacak. Enerji miktarı ötelenebilir yükün enerjisine eşleninceye
ötelenebilir yük çalışmaya başlayacak.

"""
