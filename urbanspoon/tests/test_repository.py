from xarray import Dataset
import os
import numpy as np
import tempfile
from urbanspoon import repository, core
from urbanspoon.tests.conftest import (
    time_series_factory,
    spatial_gcm_factory,
)


def test_read_dataset():
    url = "memory://test_read_dataset.zarr"  # writing in memory FS -- don't assign same names throughout tests.
    Dataset({"bar": 321}).to_zarr(url)
    actual = repository.read_dataset(url)
    expected = Dataset({"bar": 123})
    assert actual == expected


def test_read_array():
    url = "memory://test_read_array.zarr"
    Dataset({"bar": 321}).to_zarr(url)  # Manually write to memory FS.
    actual = repository.read_array(url, "bar")
    expected = np.array(321)
    np.testing.assert_equal(actual, expected)


def test_write_colored_maps():

    fakedata = {"A": spatial_gcm_factory(), "B": spatial_gcm_factory()}
    with tempfile.NamedTemporaryFile() as outfile:
        repository.write_plot(
            out=f"{outfile.name}.png",
            format="png",
            plot_func=core.plot_colored_maps,
            da=fakedata,
            common_title="sometitle",
            units="someunits",
            color_bar_range=(0, 1),
        )
        assert os.path.isfile(f"{outfile.name}.png")


def test_write_colored_timeseries():

    fakedata = {
        "A": {
            "temporal_data": time_series_factory(),
            "linestyle": ":",
            "color": "blue",
        },
        "B": {
            "temporal_data": time_series_factory(),
            "linestyle": ":",
            "color": "black",
        },
    }

    with tempfile.NamedTemporaryFile() as outfile:
        repository.write_plot(
            out=f"{outfile.name}.png",
            format="png",
            plot_func=core.plot_colored_timeseries,
            da=fakedata,
            title="sometitle",
            units="someunits",
        )
        assert os.path.isfile(f"{outfile.name}.png")
