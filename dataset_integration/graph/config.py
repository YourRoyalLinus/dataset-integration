import matplotlib.pyplot as plt
from ._graph_config import _GraphConfig, GRAPH_CONFIGS, PLT_CONFIGS
from ._graph_decos import graph_colors

_GLOBAL_GRAPH_CONFIGS = _GraphConfig(PLT_CONFIGS)

def _get_graph_configs(user_input :str) -> _GraphConfig:
    """Return a _GraphConfig object based on _graph args from the command
    line parser. The user_input is separated by the "|" character. Ordering
    from user_input must be preserved as follows:
        0: xlabel
        1: ylabel
        2: title
        3: color
    
    Positional Arguments:
        user_input : str
            - value returned from --source_graph or --integrated_graph command
            line args
    """
    graph_config = _GraphConfig(GRAPH_CONFIGS)
    if user_input:
        config_list = [input.strip() for input in user_input.split("|")]
        
        graph_config["xlabel"] = config_list[0]
        graph_config["ylabel"] = config_list[1]
        graph_config["title"] = config_list[2]
        graph_config["color"] = config_list[3]

    return graph_config

@graph_colors
def _is_valid_color(colors :dict, user_color :str):
    """Returns true if user_color is a graph color provided by matplotlib

    Positional Arguments:
        colors : dict
            - dict of all colors supported by matplotlib passed in
            by the graph_colors decorator
        user_color : str
            - a string representing the name of a color
    """
    try:
        colors[user_color]
    except KeyError:
        return False
    return True

def _configure_plot(configs :_GraphConfig) -> None:
    """Function to globally configure the underlying matplotlib module by
    passing a dictionary of configs

    Positional Arguments
        configs : _GraphConfig
            - A dictionary of matplotlib configs. Key represents the attr
            and value is a tuple that will be unpacked and passed to plt.attr
    """
    for key, value in configs.items():
        if hasattr(plt, key):
            getattr(plt, key)(*value)
        else:
            print(f'matplotlib has no property: {key}')
    
    return None

def _configure_graph(axis :plt.Axes, graph_configs :_GraphConfig) -> None:
    """Function to configure graph on the axis passed in
    
    Positional Arguments
        axis : matplotlib.Axes
            - The matplotlib object representing the axes of a graph
        graph_configs : _GraphConfig
            - _GraphConfig object representing user defined configurations

    Graph Configs:
        - xlabel
        - ylabel
        - title
    
    The function also changes the ticklabel format from scientific notation
    to plain and calls axis.grid() to display a grid
    """
    axis.set(xlabel=graph_configs["xlabel"], ylabel=graph_configs["ylabel"],
            title=graph_configs["title"])

    axis.ticklabel_format(style='plain')
    axis.grid()
    
    return None