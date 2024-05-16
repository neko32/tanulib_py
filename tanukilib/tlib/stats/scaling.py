from numpy.typing import NDArray
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def scale_by_minmax(a: NDArray) -> NDArray:
    """Scale array by min-max"""
    mms = MinMaxScaler()
    return mms.fit_transform(a)


def scale_by_standardization(a: NDArray) -> NDArray:
    """Scale array by standardization"""
    std = StandardScaler()
    return std.fit_transform(a)
