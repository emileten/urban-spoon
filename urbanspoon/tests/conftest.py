import numpy as np
import xarray as xr

#TODO convert all that stuff to pytest.fixtures

def write_dataset(ds, url_or_path):
    """
    Writes dataset. Testing purpose.

    Parameters
    ----------
    ds : xr.Dataset
    url_or_path : str
    """
    ds.to_zarr(url_or_path, mode="w")


def time_series_factory(x=np.random.rand(365), start_date="1995-01-01"):

    if x.ndim != 1:
        raise ValueError("'x' needs dim of one")

    time = xr.cftime_range(
        start=start_date, freq="D", periods=len(x), calendar="standard"
    )

    return xr.DataArray(x, {"time": time}, ["time"])


def spatial_gcm_factory(
    x=np.random.rand(721, 361),
    lat=np.arange(-90, 90.5, 0.5),
    lon=np.arange(-180, 180.5, 0.5),
):

    return xr.DataArray(x, {"lon": lon, "lat": lat}, ["lon", "lat"])


def spatio_temporal_gcm_factory(
    x=np.random.rand(1, 361, 721),
    start_date="1995-01-01",
    lat=np.arange(-90, 90.5, 0.5),
    lon=np.arange(-180, 180.5, 0.5),
    units="someunit"
):

    time = xr.cftime_range(
        start=start_date, freq="D", periods=len(x), calendar="standard"
    )
    out = xr.DataArray(
        data=x, coords={"time": time, "lat": lat, "lon": lon}, dims=["time", "lat", "lon"], attrs={"units": units}
    )

    return out
