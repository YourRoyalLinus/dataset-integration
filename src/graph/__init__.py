"""Package that wraps matplotlib to configure and display graphs"

Classes:
    _GraphConfig (implementation detail)
        - object to represent matplotlib configurations

Modules:
    _graph_decos (implementation detail)
        - contains decorators used for the config module
    _graph_config
        - contains _GraphConfig class, and the _GRAPH_CONFIG dict and 
        _PLT_CONFIG global graph variables
    config
        - contains functions to configure graph.py
    graph
        - contains functions to plot and display the matplotlib graphs
"""

from . import config
from . import graph

__all__ = ["config", "graph"]