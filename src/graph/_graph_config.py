#Dictionary of user graph configurations
GRAPH_CONFIGS = {
    "xlabel": None, 
    "ylabel": None, 
    "title": None, 
    "color": None
}

#Global configurations for matplotlib module
PLT_CONFIGS = {
    "subplots_adjust":(.125,.11,.9,.9,.2,.55)
}

class _GraphConfig(dict):
    """A class that wraps a dict to represent graph configuration objects

    Methods:
        __init__(self, mapping)
            - Defer to dict.__init__(mapping)
        __setitem__(self, key, value)
            - Defer to dict.__setitem__(key, value)
        __delitem(self, key)
            - Defer to dict__delitem(key)
    """
    def __init__(self, mapping):
        super().__init__(mapping)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __delitem__(self, key):
        super().__delitem__(key)
