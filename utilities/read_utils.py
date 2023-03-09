import pandas


def get_csv_as_list(filepath):
    data = pandas.read_csv(filepath_or_buffer=filepath, delimiter=";")
    return data.values.tolist()
