import xlrd3

workbook = xlrd3.open_workbook('test02.xlsx')
sheet = workbook.sheet_by_name('Sheet1')

def get_cell_merged_value(row_index,col_index):
    cell_value = None
    for (min_row, max_row, min_col, max_col) in sheet.merged_cells:
        if row_index >= min_row and row_index < max_row:
            if col_index >= min_col and col_index < max_col:
                cell_value = sheet.cell_value(min_row, min_col)  # 合并单元格的值等于合并起点的值（第一个单元格的值）
                break;
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value

for i in range(0,9):
    for j in range(0,4):
        cell_value = get_cell_merged_value(i,j)
        print(cell_value,end=' ')  # 换行处理
    print()