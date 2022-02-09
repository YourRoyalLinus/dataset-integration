import matplotlib.colors as mcolors

def graph_colors(func :callable):
    """A decorator function to pass a dict of all colors supported by 
    matplotlib into the wrapped function
    """
    colors = {**mcolors.BASE_COLORS, 
                    **mcolors.TABLEAU_COLORS,
                        **mcolors.CSS4_COLORS,
                            **mcolors.XKCD_COLORS}   
    def inner(user_color: str): 
        return func(colors, user_color)
    return inner
