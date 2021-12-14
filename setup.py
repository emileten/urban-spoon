from setuptools import setup

setup(
    name='urbanspoon',
    version='1.1',
    packages=['urbanspoon'],
    url='https://github.com/emileten/urbanspoon',
    license='Apache 2.0',
    author='Emile Tenezakis',
    author_email='e.tenezakis@gmail.com',
    description='validating downscaleCMIP6',
    install_requires=[
        "xclim @ git+https://github.com/ClimateImpactLab/xclim@63023d27f89a457c752568ffcec2e9ce9ad7a81a",
        "matplotlib",
        "xarray",
        "gcsfs",
        "numpy",
        "matplotlib",
        "cartopy",
        "pytest",
        "black",
        "nc-time-axis",
        "zarr",
        "dask"
    ],
)
