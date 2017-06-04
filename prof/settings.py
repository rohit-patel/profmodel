####PROF SPECIFIC SETTINGS####

BU_column_name = 'Business Unit'



Transaction_desiredColumns=('Transaction Number', 'Transaction Date', BU_column_name, 'Customer Number', 'Customer Name', 'Product Number', 'Quantity',
                'List Price', 'Total Price', 'Discount', 'Invoice Amount')
Transaction_modelFields=('TransactionNumber', 'TransactionDate', 'BusinessUnit', 'CustomerNumber', 'CustomerName', 'ProductNumber', 'Quantity',
                'ListPrice', 'TotalPrice', 'Discount', 'InvoiceAmount')  #These are the names of columns in the model, do not change here
TransactionSheetName = 'TransactionData'
Transaction_column_names_to_model_dict = dict(zip(Transaction_desiredColumns,Transaction_modelFields))

PnL_revenueMarkers=['Total Revenue', 'Total Rev', 'Net Rev', 'Net Revenue']
PnL_sample_line_descriptions=['Sales', 'Sales Returns (Reduction)', 'Sales Discounts (Reduction)', 'Other Revenue 1', 'Other Revenue 2', 'Other Revenue 3', '…', 'Net Revenue', '', 'Material 1', 'Material 2', '..', 'Direct Material', '', 'Labor', 'Labor Overtime', '…', 'Direct Labor', '', 'Other Direct Cost 1', '…', '…', '…', '…', 'Cost of Goods Sold', '', 'Gross Profit', '', 'Rent', 'Office Supplies', 'Utilities', 'Telephone', 'Insurance', 'Travel', 'Maintenance', 'Advertising', 'Other 1', 'Other 2', 'Other 3', '…', '…', 'EBITDA', '', '', 'Depreciation', 'Amortization', '…', '', 'Operating Income (EBIT)', '', '', 'Interest Expense (Income)', 'Income Tax Expense', '…', '…', '', '', 'Net Income']
PnL_sample_line_codes=['R10001014', 'R10001015', 'R10001016', 'R10001017', 'R10001018', 'R10001019', 'R10001020', '', '', 'C10001023', 'C10001024', 'C10001025', '', '', 'C10001028', 'C10001029', 'C10001030', '', '', 'C10001033', 'C10001034', 'C10001035', 'C10001036', 'C10001037', '', '', '', '', 'C10001044', 'C10001045', 'C10001046', 'C10001047', 'C10001048', 'C10001049', 'C10001050', 'C10001051', 'C10001052', 'C10001053', 'C10001054', 'C10001022', 'C10001027', '', '', '', 'C10001043', 'C10001032', '', '', '', '', '', 'C10001057', 'C10001059', 'C10001061', 'C10001062', '', '', '']    
PnL_sample_line_aggregate_status=[0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]
PnL_leading_column_names=['Line Description', 'Line Code']
PnL_total_column_name='All Months'
PnL_aggregate_sheet_name = 'All BUs'
PnL_revenue_or_cost_column_name = 'RevorCost'
PnL_aggregate_line_flag_column_name = 'Aggregate'
PnL_period_column_name = 'Period'
PnL_amount_column_name = 'Amount'
PnL_column_names_to_model_dict = dict(zip(PnL_leading_column_names,['LineDescription', 'LineCode'])) #The list on the right are the name of the fields in the model, should not be changed here
PnL_column_names_to_model_dict[PnL_revenue_or_cost_column_name]='RevorCost'  #The string on the right is the name of the field in the model, should not be changed here
PnL_column_names_to_model_dict[PnL_aggregate_line_flag_column_name]='Aggregate'  #The string on the right is the name of the field in the model, should not be changed here
PnL_column_names_to_model_dict[PnL_period_column_name]='Period'  #The string on the right is the name of the field in the model, should not be changed here
PnL_column_names_to_model_dict[PnL_amount_column_name]='Amount'  #The string on the right is the name of the field in the model, should not be changed here
Key_last_col_name = 'Aggregate'

Key_settings_dict = { 'last_col_name' : Key_last_col_name}


Transactions_settings_dict = { 'desiredColumns' : Transaction_desiredColumns,
        'TransactionSheetName' : TransactionSheetName,
        'column_names_to_model_dict' : Transaction_column_names_to_model_dict
}

PnL_settings_dict={'revenueMarkers':PnL_revenueMarkers,
         'sample_line_descriptions':PnL_sample_line_descriptions,
         'sample_line_codes' : PnL_sample_line_codes,
         'sample_line_aggregate_status': PnL_sample_line_aggregate_status,
         'leading_column_names' : PnL_leading_column_names,
         'total_column_name' : PnL_total_column_name,
         'aggregate_sheet_name' : PnL_aggregate_sheet_name,
         'revenue_or_cost_column_name' : PnL_revenue_or_cost_column_name,
         'aggregate_line_flag_column_name' : PnL_aggregate_line_flag_column_name,
         'BU_column_name' : BU_column_name,
         'period_column_name' : PnL_period_column_name,
         'amount_column_name' : PnL_amount_column_name,
         'column_names_to_model_dict' : PnL_column_names_to_model_dict
}


