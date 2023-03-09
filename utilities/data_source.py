from read_utils import get_csv_as_list

test_invalid_login_data = get_csv_as_list("../test_data/test_invalid_login_data.csv")

test_add_employee_data = [("Admin", "admin123", "John", "J", "Wick", "John Wick", "John"),
                          ("Admin", "admin123", "Peter", "J", "Wick", "Peter Wick", "Peter")]
