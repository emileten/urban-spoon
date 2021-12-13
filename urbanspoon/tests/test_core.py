import numpy as np
from urbanspoon import core
import xarray as xr


def _timeseriesfactory():
    x = np.random.rand(365)

    start_time = str("1995-01-01")
    if x.ndim != 1:
        raise ValueError("'x' needs dim of one")

    time = xr.cftime_range(
        start="1995-01-01", freq="D", periods=len(x), calendar="standard"
    )

    return xr.DataArray(x, {"time": time}, ["time"])


def _gcmfactory():

    lat = range(start=-90, stop=90.5, step=0.5)
    lon = range(start=-180, stop=180.5, step=0.5)
    x = np.random.rand(len(lon), len(lat))
    return xr.DataArray(x, {"lon": lon, "lat": lat}, ["lon", "lat"])


def test_plot_colored_maps():
    """
    Checking it runs
    """
    fakedata = {"A": gcmfactory(), "B": gcmfactory()}
    core.plot_colored_maps(
        ds=fakedata, title="sometitle", units="someunits", color_bar_range=(0, 1)
    )


def plot_colored_timeseries():

    """
    Checking it runs
    """
    fakedata = {
        "A": {"temporal_data": timeseriesfactory(), "linestyle": ":"},
        "B": {"temporal_data": timeseriesfactory(), "linestyle": ":"},
    }

    core.plot_colored_timeseries(fakedata, "sometitle", "someunits")
