import xlrd

path = r'C:\Users\KIIT\PycharmProjects\SeleniumAssignment(18-03-2026)\general_utilities\details.xlsx'


def excel_dt():
    workbook = xlrd.open_workbook(path)             ## Book object
    worksheet = workbook.sheet_by_name("Sheet1")       ## sheet object
    rows = worksheet.get_rows()                     ## generator object
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value
    return d
