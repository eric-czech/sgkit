from typing import Any, Union

import dask.array as da
import numpy as np
import xarray as xr

DType = Any
ArrayLike = Union[np.ndarray, da.Array, xr.DataArray]
