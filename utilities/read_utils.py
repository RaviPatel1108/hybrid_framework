import pandas


def get_csv_as_list(filepath):
    df = pandas.read_csv(filepath_or_buffer=filepath, delimiter=";")
    return df.values.tolist()


def get_sheet_as_list(file_path, sheet_name):
    df = pandas.read_excel(io=file_path, sheet_name=sheet_name)
    return df.values.tolist()


def get_value_from_json(file_path, key):
    dic = pandas.read_json(path_or_buf=file_path, typ="dictionary")
    return dic[key]
