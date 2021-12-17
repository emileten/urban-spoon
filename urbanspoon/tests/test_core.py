import numpy as np
import pytest
from urbanspoon.tests.conftest import (
    time_series_factory,
    spatio_temporal_gcm_factory,
    spatial_gcm_factory,
)
from urbanspoon import core


def test_xr_average_across_days_of_year():

    fakedata = spatio_temporal_gcm_factory(
        x=np.array([1, 2, 3, 4])[:, np.newaxis, np.newaxis],
        lat=np.ones(1),
        lon=np.ones(1),
    )
    actual = core.xr_average_across_days_of_year(fakedata)
    assert actual.shape == (1, 1, 1)
    assert actual.values[0, 0, 0] == 2.5


def test_apply_xr_collapse_across_time():
    fakedata = spatio_temporal_gcm_factory(
        x=np.ones(720)[:, np.newaxis, np.newaxis], lat=np.ones(1), lon=np.ones(1)
    )
    actual = core.apply_xr_collapse_across_time(
        fakedata, [("1995", "1996"), ("1996", "1997")]
    )
    assert all(x in actual for x in ["1995_1996", "1996_1997"])
    assert actual["1995_1996"].shape == (1, 1)
    assert actual["1995_1996"].values[0, 0] == 1


def test_xr_collapse_across_time():

    fakedata = spatio_temporal_gcm_factory(
        x=np.array([1, 2, 3, 4])[:, np.newaxis, np.newaxis],
        lat=np.ones(1),
        lon=np.ones(1),
    )
    actual = core.xr_collapse_across_time(fakedata, ("1995-01-01", "1995-01-02"))
    assert actual.shape == (1, 1)
    assert actual.values[0, 0] == 1.5


def test_xr_collapse_across_space():
    fakedata = spatial_gcm_factory(
        x=np.array([[1, 2], [3, 4]]), lat=np.array([1, 2]), lon=np.array([1, 2])
    )
    num = (
        1 * np.cos(1 * np.pi / 180.0)
        + 2 * np.cos(2 * np.pi / 180.0)
        + 3 * np.cos(1 * np.pi / 180.0)
        + 4 * np.cos(2 * np.pi / 180.0)
    )
    den = np.cos(1 * np.pi / 180.0) * 2 + np.cos(2 * np.pi / 180.0) * 2
    expected = num / den
    actual = core.xr_collapse_across_space(fakedata)
    assert actual.shape == ()
    np.testing.assert_almost_equal(expected, actual.values.item())

@pytest.mark.skip(reason="unimplemented")
def test_xr_collapse_to_global_time_series():

    # TODO
    raise NotImplementedError


@pytest.mark.skip(reason="unimplemented")
def test_xr_count_across_days_of_year():

    # TODO
    raise NotImplementedError


@pytest.mark.skip(reason="unimplemented")
def test_xc_maximum_consecutive_dry_days():

    # TODO
    raise NotImplementedError


@pytest.mark.skip(reason="unimplemented")
def test_xc_rx5day():

    # TODO
    raise NotImplementedError


def test_plot_colored_maps():
    """
    Checking it runs
    """
    fakedata = {"A": spatial_gcm_factory(), "B": spatial_gcm_factory()}
    core.plot_colored_maps(
        da=fakedata, common_title="sometitle", units="someunits", color_bar_range=(0, 1)
    )


def test_plot_colored_timeseries():

    """
    Checking it runs
    """
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

    core.plot_colored_timeseries(da=fakedata, title="sometitle", units="someunits")
