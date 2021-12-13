import numpy as np
import xarray as xr

def time_series_factory(x=np.random.rand(365), start_date="1995-01-01"):

    if x.ndim != 1:
        raise ValueError("'x' needs dim of one")

    time = xr.cftime_range(
        start=start_date, freq="D", periods=len(x), calendar="standard"
    )

    return xr.DataArray(x, {"time": time}, ["time"])


def spatial_gcm_factory(x=np.random.rand(721, 361), lat=np.arange(-90, 90.5, 0.5), lon=np.arange(-180, 180.5, 0.5)):

    return xr.DataArray(x, {"lon": lon, "lat": lat}, ["lon", "lat"])


def spatio_temporal_gcm_factory(x=np.random.rand(721, 361), start_date="1995-01-01", lat=np.arange(-90, 90.5, 0.5), lon=np.arange(-180, 180.5, 0.5)):

    time = xr.cftime_range(
        start=start_date, freq="D", periods=len(x), calendar="standard"
    )
    return xr.DataArray(x, {"time": time, "lat": lat, "lon": lon}, ["time", "lat", "lon"])
