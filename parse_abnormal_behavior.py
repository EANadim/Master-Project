# import pandas as pd

# def parse_abnormal_behavior(coding_sheet_name): 
#     sheets_dict= pd.read_excel(coding_sheet_name, sheet_name=None)
#     def is_numeric(value):
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#     for  name, df_sheet in sheets_dict.items():
#         abnormal_behavior_col = df_sheet.iloc[:, 7]

#         # Check for numerical values in the column and filter the rows
#         numerical_rows = df_sheet[abnormal_behavior_col.apply(lambda x: isinstance(x, (int, float, complex)) and not isinstance(x, bool))]
        
#         # rows with numerical values in the specified column
#         if not numerical_rows.empty:
#             print(numerical_rows)


# coding_sheet_name_1 = "coding_ehtesham.xlsx"
# coding_sheet_name_2 = "coding_usman.xlsx"

# parse_abnormal_behavior(coding_sheet_name_1)
# # parse_abnormal_behavior(coding_sheet_name_2)
