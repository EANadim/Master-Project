# import pandas as pd

# def parse_abnormal_behavior(coding_sheet_name): 
#     sheets_dict= pd.read_excel(coding_sheet_name, sheet_name=None)
    
#     for name, df_sheet in sheets_dict.items():
#         numeric_col = pd.to_numeric(df_sheet.iloc[:, 7], errors='coerce')

#         # Filter rows where the conversion was successful (i.e., not NaN)
#         filtered_rows = df_sheet[numeric_col.notna()]

#         print(filtered_rows.items())


# coding_sheet_name_1 = "./coding_archive/latest/coding_ehtesham.xlsx"
# coding_sheet_name_2 = "./coding_archive/latest/coding_usman.xlsx"

# parse_abnormal_behavior(coding_sheet_name_1)
# # parse_abnormal_behavior(coding_sheet_name_2)
