def filter_query(param, data):
    return filter(lambda x: param in x, data)


def map_query(param, data):
    col_number = int(param)
    return map(lambda x: x.split(" ")[col_number], data)


def sort_query(param, data):
    return sorted(data, reverse=param == "desc")


def unique_query(data, *args, **kwargs):
    return set(data)


def limit_query(param, data):
    limit = int(param)
    return data[:limit]
