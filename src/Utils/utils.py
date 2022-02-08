def get_graph_configs(user_input :str) -> dict:
    configs = {"xlabel": None, "ylabel": None, "title": None}
    if user_input:
        config_list = [input.strip() for input in user_input.split("|")]
    
        configs["xlabel"] = config_list[0]
        configs["ylabel"] = config_list[1]
        configs["title"] = config_list[2]

    return configs
