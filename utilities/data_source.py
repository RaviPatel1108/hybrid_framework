from utilities import read_utils

test_invalid_login_data = read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")

# test_add_employee_data = [("Admin", "admin123", "John", "J", "Wick", "John Wick", "John"),
#                           ("Admin", "admin123", "Peter", "J", "Wick", "Peter Wick", "Peter")]

test_add_employee_data = read_utils.get_sheet_as_list("../test_data/orange_test_data.xlsx", "test_add_valid_employee")


test_invalid_file_upload = read_utils.get_sheet_as_list("../test_data/orange_test_data.xlsx", "test_invalid_profile_upload")

