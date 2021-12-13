import xarray as xr
import logging
from urbanspoon import core
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)


def read_dataset(url_or_path):
    """Read Dataset from Zarr store

    Parameters
    ----------
    url_or_path : str
        Location of Zarr store to read.

    Returns
    -------
    xr.Dataset
    """
    logger.debug(f"Reading {url_or_path}")
    x = xr.open_zarr(url_or_path)
    logger.info(f"Read {url_or_path}")
    return x


def read_array(url_or_path, var):
    """Read Dataset from Zarr store and pull array.

    Parameters
    ----------
    url_or_path : str
        Location of Zarr store to read.
    var: str

    Returns
    -------
    xr.DataArray
    """
    return read_dataset(url_or_path)[var]


def write_colored_maps(out, format, **kwargs):
    """
    runs core.plot_colored_maps and writes to disk a given representation of it.

    Parameters
    ----------
    out : str
        path where to write the file
    format : str
        'png'
    kwargs :
        additional arguments passed to core.plot_colored_maps
    """

    core.plot_colored_maps(**kwargs)
    plt.savefig(fname=out, format=format)


def write_colored_timeseries(out, format, **kwargs):
    """
    runs core.plot_colored_timeseries and writes to disk a given representation of it.

    Parameters
    ----------
    out : str
        path where to write the file
    format : str
    kwargs :
        additional arguments passed to core.plot_colored_timeseries
    """

    core.plot_colored_timeseries(**kwargs)
    plt.savefig(fname=out, format=format)
