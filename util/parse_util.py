def parse_str_to_int(value_dict):
    for key in value_dict.keys():
        value_dict[key] = int(value_dict[key])
    return value_dict
