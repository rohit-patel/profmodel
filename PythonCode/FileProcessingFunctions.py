def ifHeaderReturnIndex(row, desiredColumns):
    '''This function checks if a particular excel row is the header row. It does so by simply checking that each of the
    column names in the desired header row appear in the row once, and exactly once. If it is a header row, the function
    returns the index of the header columms as a tuple. If not, it retruns the python 'None' object. The arguments are:
    1. An openpyxl worksheet
    2. A tuple of strings - the column headers'''
    rowtuple=tuple(cell.value for cell in row)
    i=True
    
    for ColumnName in desiredColumns:
        if rowtuple.count(ColumnName) != 1: i=False
    if i==False:
        return None
    else:
        a=list()
        for i in desiredColumns:
            a.append(rowtuple.index(i))
        return tuple(a)
    
    
def isRowValid(row,index):
    '''Determines if the row is a valid data row. For the moment, simply checks if the first column dicted by selectedIndex is empty.'''
    return bool(row[index[0]].value)
