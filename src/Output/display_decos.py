import matplotlib.colors as mcolors

def plt_colors(func :callable):
    def inner(user_color: str):
        colors = {**mcolors.BASE_COLORS, 
                    **mcolors.TABLEAU_COLORS,
                        **mcolors.CSS4_COLORS,
                            **mcolors.XKCD_COLORS}     
        return func(colors, user_color)
    return inner
