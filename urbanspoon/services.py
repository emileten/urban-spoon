from urbanspoon import core, repository


def map_bidecadal_time_average(
    inputfile, var, color_bar_range, outputfile, format="png"
):

    """
    Produces a series of maps colored by bidecadal averages of 'var' from an input dataset path
    """

    da = repository.read_array(inputfile, var)
    da_dict = core.xr_bidecadal_time_average(da)
    core.plot_colored_maps(
        da=da_dict,
        common_title=f"{var} bidecadal average",
        units=da.attrs["units"],
        color_bar_range=color_bar_range,
    )
    repository.write_colored_maps(out=outputfile, format=format)
