from _collections_abc import Sequence
from typing import Dict
import matplotlib.pyplot as plt
from .display_decos import plt_colors

@plt_colors
def _is_valid_color(colors :dict, user_color :str):
    try:
        colors[user_color]
    except KeyError:
        return False
    return True

def _configure_plot(configs :dict) -> None:
    for key, value in configs.items():
        if hasattr(plt, key):
            getattr(plt, key)(*value)
        else:
            print(f'matplotlib has no property: {key}')
    
    return None

def _configure_graph(axis :plt.Axes, user_config :dict) -> None:
    axis.set(xlabel=user_config["xlabel"], ylabel=user_config["ylabel"],
            title=user_config["title"])

    axis.ticklabel_format(style='plain')
    axis.grid()
    
    return None

def _plot_graph(axes :plt.Axes, user_config :dict, x :Sequence, y :Sequence) \
            -> None:

    if user_config["color"] and _is_valid_color(user_config["color"].lower()):
        axes.plot(x, y, color=user_config["color"].lower())
    else:
        axes.plot(x, y)

    return None

def _show_graph() -> None:
    plt_configs = {"subplots_adjust":(.125,.11,.9,.9,.2,.55)}
    _configure_plot(plt_configs)
    plt.show()
    
    return None
    
def graph(x_values :Sequence, y_values: Sequence, integrated_values : Sequence,
        source_config: dict, integrated_config :dict) -> None:
    
    figs, axs = plt.subplots(2)
    for i in range(0, 2):
        if i == 0:
            _configure_graph(axs[i], source_config)
            _plot_graph(axs[i], source_config, x_values, y_values)
        elif i == 1:
            _configure_graph(axs[1], integrated_config)
            _plot_graph(axs[i], integrated_config, x_values, integrated_values)

    _show_graph()

    return None




