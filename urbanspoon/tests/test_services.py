import os
import xarray as xr
import numpy as np
import tempfile
from urbanspoon import services, repository
from urbanspoon.tests import conftest

def test_write_map_periods_average():
    fakedata = xr.Dataset({'fakevariable':conftest.spatio_temporal_gcm_factory(np.random.rand(4, 361, 721))})
    fakedata_storage = "memory://fakedata_map_periods_average.zarr"
    repository.write_dataset(ds=fakedata, url_or_path=fakedata_storage)
    with tempfile.NamedTemporaryFile() as outfile:
        services.write_map_period_average(inputfile=fakedata_storage, var="fakevariable", color_bar_range=(0, 1), outputfile=f"{outfile.name}.png", periods=[("1995-01-01","1995-01-02"),("1995-01-03","1995-01-04")])
        assert os.path.isfile(f"{outfile.name}.png")

