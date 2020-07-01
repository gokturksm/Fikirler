import pandas as pd

value_list = ['fromP2P', 'toP2P', 'fromGRID', 'toGRID']

df_pv = pd.Series([50, 50, 50, 50], name="time")
df_loads = pd.DataFrame([[0, 0, 0, 0],
                         [0, 10, 15, 20],
                         [0, 10, 60, 55],
                         [99, 99, 99, 99]], columns=['h1', 'h2', 'h3', 'h4'])


def make_df_header(loads_list, values_list):
    return pd.DataFrame([], columns=pd.MultiIndex.from_product([values_list, loads_list.columns]))


def make_equal(series: pd.Series, matched: float) -> pd.Series:
    """
    Equally distrubute a series considering a matched value.
    Lower values than matched value are filtered.
    :param series: A series which has one or more rows.
    :param matched: A positive float number.
    :return: A series that is equally distrubuted.
    """
    check_negative = series.sum() < 0
    if check_negative:
        sorted_ = series.abs().sort_values()
    else:
        sorted_ = series.sort_values()
    per_ = matched / series.size
    for i, v in enumerate(sorted_):
        if not v > per_:
            per_ = (matched - sorted_.iloc[:i + 1].sum()) / (series.size - (i + 1))
        else:
            break
    sorted_.iloc[i:] = per_
    if check_negative:
        return series.mul(0).add(sorted_).mul(-1)
    else:
        return series.mul(0).add(sorted_)


# geçici kwar değerlerini silmeyi unutma, gölgeleyenleri!
def create_good_df(pv_: float, loads_: pd.Series) -> pd.Series:
    """
    Creates one row of PV usage data.
    """
    time_ = loads_.name
    after_pv = loads_.sub(pv_ / loads_.size)
    buyers = after_pv.loc[after_pv >= 0.0]
    sellers = after_pv.loc[after_pv < 0.0]
    p2p_ = min(abs(sellers.sum()), buyers.sum())
    non_p2p_ = after_pv.sum()
    if p2p_ > 0:  # if p2p is happening before grid
        if non_p2p_ < 0:  # community is net seller
            p2p_sellers = make_equal(sellers, p2p_)
            p2p_buyers = buyers
        elif non_p2p_ > 0:  # community is net buyer
            p2p_sellers = sellers
            p2p_buyers = make_equal(buyers, p2p_)
        else:  # community is neuteral
            p2p_sellers, p2p_buyers = sellers, buyers
    else:  # no p2p is happened, so now we head for the grid
        p2p_sellers, p2p_buyers = sellers.mul(0.0), buyers.mul(0.0)
    grid_sellers = sellers - p2p_sellers
    grid_buyers = buyers - p2p_buyers
    p2p_buyers.name, p2p_sellers.name = 'fromP2P', 'toP2P'
    grid_buyers.name, grid_sellers.name = 'fromGRID', 'toGRID'
    # make them all same sized
    row_series = pd.DataFrame(data=[p2p_buyers, p2p_sellers, grid_buyers, grid_sellers]
                              ).sort_index(axis=1).T.unstack()
    row_series.name = time_
    return row_series


df__ = make_df_header(df_loads, value_list)
for ii in range(df_pv.size):
    df__ = df__.append(create_good_df(df_pv.iloc[ii], df_loads.iloc[ii]))

