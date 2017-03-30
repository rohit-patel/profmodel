#Openpyxl imports
from openpyxl import load_workbook, Workbook, cell
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.utils import get_column_letter
from openpyxl.writer.excel import save_virtual_workbook


#Database imports
from django.db import transaction
from prof.models import FileSpace, RunSpace, TransactionData
#from __future__ import unicode_literals
from django.core.files.base import ContentFile

#Global constants import
from prof.settings import desiredColumns, transactionSheetName, PnL_cunstructor_dict

#Other imports
from datetime import date, timedelta, datetime


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


@transaction.atomic
def ProcessTransactionData(fileObject, run, sheetName=transactionSheetName,keyFileObject=None):
    """ This function takes the file object, the name of the sheet in which the data is stores, and loads the transaction data into the Django model TransactionData."""
    if not(keyFileObject): keyFileObject = fileObject
    wb=load_workbook(fileObject.file, read_only=True, data_only=True)
    ws=wb.get_sheet_by_name(sheetName)
    selectedIndex=None
    for row in ws.rows:
        if selectedIndex:
            if isRowValid(row,selectedIndex):
                newrow=[row[i].value for i in selectedIndex]
                dictionary=dict(zip(outputColumnNames,newrow))
                dictionary['run']=run
                dictionary['SourceFileObject']=keyFileObject
                TransactionData(**dictionary).save()
        else:
            if ifHeaderReturnIndex(row,desiredColumns):
                selectedIndex=ifHeaderReturnIndex(row, desiredColumns)
                outputColumnNames=[row[i].value.replace(" ", "") for i in selectedIndex]


def revCells(row):
    '''This is formatting for a row that carries revenue.'''
    for cell in row:
        cell.fill=PatternFill(start_color='d2fedb', end_color='d2fedb', fill_type='solid')

def costCells(row):
    '''This is formatting for a row that carries costs.'''
    for cell in row:
        cell.fill=PatternFill(start_color='ffe8e8', end_color='ffe8e8', fill_type='solid')

def headerCells(row):
    '''This is formatting for a row that has column names.'''
    for cell in row:
        cell.fill=PatternFill(start_color='ffff00', end_color='ffff00', fill_type='solid')
        cell.font=Font(bold=True)

def makeBold(row):
    '''This function makes a row bold'''
    for cell in row:
        cell.font=Font(bold=True)


def fixWidth(ws):
    '''
    This function takes an openpyxl worksheet as an input and returns an openpyxl worksheet after setting the column
    width for columns in the sheet at the maximum of the length of the string in any of the cells in the column.
    '''
    column_widths = []
    for row in ws:
        for i, cell in enumerate(row):
            if len(column_widths) > i:
                if len(str(cell.value))+2 > column_widths[i]:
                    column_widths[i] = len(str(cell.value))+2
            else:
                column_widths += [len(str(cell.value))+2]

    for i, column_width in enumerate(column_widths):
        ws.column_dimensions[get_column_letter(i+1)].width = column_width
        
def isRevAggregate(row,index,revenueMarkers):
    '''
    This function simply determined if a row in the PnL is a "Net Revenue" row, mostly used for stlying purposes.
    Presently, it simply looks at the text in the firxt column and checks if any of the markets are present.
    '''
    mark=False
    for marker in revenueMarkers:
        if marker in row[index[0]].value: mark=True
    return mark
    
def applyPnLStyling(ws,pnl_column_names,revenueMarkers):
    headerfound=False
    Revenue=True
    for row in ws.rows:
        if headerfound and Revenue:
            revCells(row)
            if isRevAggregate(row,selectedIndex,revenueMarkers): Revenue = False
        elif headerfound and not(Revenue):
            costCells(row)
        elif ifHeaderReturnIndex(row,pnl_column_names):
            headerCells(row)
            selectedIndex=ifHeaderReturnIndex(row, pnl_column_names)
            headerfound=True
        else:
            makeBold(row)
    

def generateSamplePnLBUSheet(run, ws, BU, cunstructor_dict = PnL_cunstructor_dict):
    '''
    This function generates a sample PnL based on the transaction data. It basically accepts the run, and the BU as
    an argument and then determines the period in which tansactions were present. It then creates a sample based
    on this determined period.'''
    
    #Determine the periods in which transacitons are present for the business unit, and create column names
    if BU == cunstructor_dict['aggregate_sheet_name']:
        period_start_date=min(x.OrderDate for x in TransactionData.objects.filter(run=run))
        period_end_date=max(x.OrderDate for x in TransactionData.objects.filter(run=run))
    else:
        period_start_date=min(x.OrderDate for x in TransactionData.objects.filter(run=run, BusinessUnit = BU))
        period_end_date=max(x.OrderDate for x in TransactionData.objects.filter(run=run, BusinessUnit = BU))
    date_extent=[period_start_date+timedelta(i) for i in range((period_end_date-period_start_date).days+1)]
    date_set=set(datetime.strftime(i,'%b-%Y') for i in date_extent)
    period_column_names = sorted(date_set, key=lambda day: datetime.strptime(day, "%b-%Y"))
    
    #Create a preamble
    preamble_rows=[['Business Unit', BU],['Period Start Date',period_start_date ],['Period End Date',period_end_date ],[]]

    #Create the list of column names
    leading_column_names=cunstructor_dict['leading_column_names']
    trailing_column_names=[cunstructor_dict['total_column_name']]
    pnl_column_names=leading_column_names+period_column_names+trailing_column_names    
    
    #Create sample body
    sample_body = [list(i) for i in zip(cunstructor_dict['sample_line_descriptions'],cunstructor_dict['sample_line_codes'])]
    
    #Append preamble to worksheet
    for row in preamble_rows:
        ws.append(row)

    #Append header
    ws.append(pnl_column_names)

    #Append body, marking the aggregate rows as bold
    for i, rowvals in [i for i in zip(cunstructor_dict['sample_line_aggregate_status'],sample_body)]:
        row=[]
        for v in rowvals:
            newcell = cell.Cell(ws,column='A', row=1,value=v)
            row.append(newcell)
        if i==1: makeBold(row)
        ws.append(row)

    #Fix column width for readability
    fixWidth(ws)

    #Apply cost and revenue coloring
    applyPnLStyling(ws,pnl_column_names,cunstructor_dict['revenueMarkers'])
    
    return(ws)
    
    
def generateSamplePnL(run, cunstructor_dict = PnL_cunstructor_dict):
    wb=Workbook()
    wb.remove_sheet(wb.active)
    BUs = set(x.BusinessUnit for x in TransactionData.objects.filter(run=run))
    BUs.add(cunstructor_dict['aggregate_sheet_name'])
    
    for BU in BUs:
        ws=wb.create_sheet(BU)
        generateSamplePnLBUSheet(run, ws, BU, cunstructor_dict)
    return(ContentFile(save_virtual_workbook(wb)))