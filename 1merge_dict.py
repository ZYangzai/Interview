def merge_dict(source_dict, update_dict):
    new_dict = {}
    if isinstance(source_dict, dict) & isinstance(update_dict, dict):
        for k1, v1 in source_dict.items():
            new_dict[k1] = v1

        for k2, v2 in update_dict.items():
            if isinstance(v2, dict) & isinstance(new_dict[k2], dict):
                new_dict[k2] = merge_dict(new_dict[k2], v2)
            else:
                new_dict[k2] = v2

        return new_dict
    elif isinstance(source_dict, dict):
        return source_dict
    elif isinstance(update_dict, dict):
        return update_dict
    else:
        return {}
