import numpy as np
from urbanspoon import core
import xarray as xr


def _timeseriesfactory():
    x = np.random.rand(365)

    if x.ndim != 1:
        raise ValueError("'x' needs dim of one")

    time = xr.cftime_range(
        start="1995-01-01", freq="D", periods=len(x), calendar="standard"
    )

    return xr.DataArray(x, {"time": time}, ["time"])


def _gcmfactory():

    lat = np.arange(-90, 90.5, 0.5)
    lon = np.arange(-180, 180.5, 0.5)
    x = np.random.rand(len(lon), len(lat))
    return xr.DataArray(x, {"lon": lon, "lat": lat}, ["lon", "lat"])


def test_plot_colored_maps():
    """
    Checking it runs
    """
    fakedata = {"A": _gcmfactory(), "B": _gcmfactory()}
    core.plot_colored_maps(
        ds=fakedata, common_title="sometitle", units="someunits", color_bar_range=(0, 1)
    )


def test_plot_colored_timeseries():

    """
    Checking it runs
    """
    fakedata = {
        "A": {"temporal_data": _timeseriesfactory(), "linestyle": ":", "color": "blue"},
        "B": {
            "temporal_data": _timeseriesfactory(),
            "linestyle": ":",
            "color": "black",
        },
    }

    core.plot_colored_timeseries(fakedata, "sometitle", "someunits")
