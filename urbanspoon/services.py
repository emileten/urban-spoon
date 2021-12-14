from urbanspoon import core, repository


def map_period_average(
    inputfile, var, color_bar_range, outputfile, periods=[("2020", "2040"), ("2040", "2060"), ("2060", "2080"), ("2080", "2100")], format="png"
):

    """
    Produces a series of maps colored by bidecadal averages of 'var' from an input dataset path.

    Parameters
    ---------
    inputfile : str
        path to data file. `var` should have units attribute inside of it.
    var : str
        variable name in dataset
    color_bar_range: tuple of float
    outputfile: str or None
        path to file containing output figure, with format suffix. If None, nothing is written to storage.
    periods: list of tuple of str
    format: str
        ignored if `outputfile` is None.
    """

    da = repository.read_array(inputfile, var)
    da_dict = core.xr_period_average(da=da, slices=periods)
    repository.write_plot(out=outputfile,
                          format=format,da=da_dict,
                          plot_func=core.plot_colored_maps,
                          common_title=f"{var} bidecadal average",
                          color_bar_range=color_bar_range,
                          units=da.attrs["units"]
                          )
