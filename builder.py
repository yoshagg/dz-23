from functions import filter_query, map_query, sort_query, unique_query, limit_query

FILE_NAME = "data/apache_logs.txt"

CMD_TO_FUNCTION = {
    "filter": filter_query,
    "map": map_query,
    "unique": unique_query,
    "sort": sort_query,
    "limit": limit_query,
}


def iter_file(file_name: str):
    with open(file_name) as file:
        for row in file:
            yield row


def query_builder(cmd, value, data):
    if data is None:
        prepared_data = iter_file(FILE_NAME)
    else:
        prepared_data = data
    result = CMD_TO_FUNCTION[cmd](param=value, data=prepared_data)
    return list(result)

    # while True:
    #     try:
    #         data = next(gen)
    #         yield data
    #     except StopIteration():
    #         break
