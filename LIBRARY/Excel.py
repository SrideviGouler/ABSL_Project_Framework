from xlrd import open_workbook
file_path=r"C:\Users\sride\PycharmProjects\ABSL_Framework_project\Data\ABSL_data.xls"
def read_locators(sheetname):
    wb = open_workbook(file_path)
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    data = { }
    for i in range(1, used_rows):
        rows = ws.row_values(i)
        data[rows[0]] = (rows[1], rows[2])
    return data

def read_headers(test_case_name, sheetname):
    wb = open_workbook(file_path)
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    for i in range(0, used_rows):
        rows = ws.row_values(i)
        if rows[0] == test_case_name:
            _headers = ws.row_values(i-1)
            _headers = [ _header for _header in _headers if _header.strip()]
            break
    return ",".join(_headers[2:])

def read_data(test_case_name, sheetname):
    data = [ ]
    wb = open_workbook(file_path)
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    for i in range(0, used_rows):
        rows = ws.row_values(i)
        if rows[0] == test_case_name:
            temp_data = [ item for item in rows if item.strip()]
            if temp_data[1].upper() == "YES":
                data.append(tuple(temp_data[2:]))
    return data
