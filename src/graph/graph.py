from _collections_abc import Sequence
from typing import Dict
import matplotlib.pyplot as plt
from .config import _GLOBAL_GRAPH_CONFIGS, _GraphConfig, _is_valid_color
from .config import _is_valid_color, _get_graph_configs
from .config import  _configure_plot, _configure_graph

def _plot_graph(axes :plt.Axes, user_config :_GraphConfig, 
                x :Sequence, y :Sequence) \
            -> None:
    """Function to plot the graph on the axis passed in. It will also change
    the color the user provided if it is a color supported by matplotlib. The 
    user-defined color is not case sensitive. If the user provided color is not
    supported, the matplotlib default is used instead (HEX #1f77b4)

    Positional Arguments:
         axis : matplotlib.Axes
            - the matplotlib object representing the axes of a graph
        graph_configs : _GraphConfig
            - _GraphConfig object representing user defined configurations
        x : Sequence
            - a sequence of values to define the x points
        y : Sequence
            - a sequence of values to define the y points
    """
    if user_config["color"] and _is_valid_color(user_config["color"].lower()):
        axes.plot(x, y, color=user_config["color"].lower())
    else:
        axes.plot(x, y)

    return None

def _show_graph() -> None:
    """Function that sets the plt configuration then calls matplotlib.show().
    plt configuration is set from _GLOBAL_GRAPH_CONFIGS
    """
    _configure_plot(_GLOBAL_GRAPH_CONFIGS)
    plt.show()
    
    return None
    
def graph(x_values :Sequence, y_values: Sequence, integrated_values : Sequence,
        source_config_str: str, integrated_config_str :str) -> None:
    """Function to configure and plot the graph of source and integrated data

    Positional Arguments:
        x_values : Sequence
            - a sequence to represent the x-values
        y_values : Sequence
            - a sequence of values to represent the y-values
        integrated_values : Sequence
            - a sequence of y-values that have been integrated
        source_config_str : str
            - A pipe-separated string that defines the configurations of
            the source data graph
        integrated_config_str : str
            - A pipe-separated string that defines the configurations of
            the integrated data graph
    
    Returns:
        NoneType, but opens a matplotlib window to display the graphs
    """
    figs, axs = plt.subplots(2)
    for i in range(0, 2):
        if i == 0:
            source_config = _get_graph_configs(source_config_str)
            _configure_graph(axs[i], source_config)
            _plot_graph(axs[i], source_config, x_values, y_values)
        elif i == 1:
            integrated_config = _get_graph_configs(integrated_config_str)
            _configure_graph(axs[1], integrated_config)
            _plot_graph(axs[i], integrated_config, x_values, integrated_values)

    _show_graph()

    return None




