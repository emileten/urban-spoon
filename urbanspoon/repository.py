import xarray as xr
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)


def write_dataset(ds, url_or_path):
    """
    Writes dataset. Testing purpose.

    Parameters
    ----------
    ds : xr.Dataset
    url_or_path : str
    """
    # TODO handle chunking
    ds.to_zarr(url_or_path, mode="w")


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


def write_plot(out, format, plot_func, **kwargs):
    """
    runs core.plot_colored_maps and writes to disk a given representation of it.

    Parameters
    ----------
    out : str
        path where to write the file
    format : str
        'png'
    plotfunc : func
    kwargs :
        arguments passed to `plotfunc`.
    """

    plot_func(**kwargs)
    plt.savefig(fname=out, format=format)
