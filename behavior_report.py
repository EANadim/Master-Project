import pandas as pd
import csv

def calculate_behavior(sheets_dict):
    individual_behaviors = []
    for  name, df_sheet in sheets_dict.items():
        try:
            individual_behavior = {}
            
            individual_behavior["participant_id"] = name
            individual_behavior["target_of_interaction"] = df_sheet[df_sheet.columns[1]].iloc[0]
            individual_behavior["sitting_distance"] = df_sheet[df_sheet.columns[1]].iloc[3]
            individual_behavior["sitting_angle"] = df_sheet[df_sheet.columns[1]].iloc[4]

            social_behavior_col = df_sheet.iloc[:, 5]
            nonsocial_behavior_col = df_sheet.iloc[:, 6]
            
            social_behavior_sum = pd.to_numeric(social_behavior_col, errors='coerce').sum()
            nonsocial_behavior_sum = pd.to_numeric(nonsocial_behavior_col, errors='coerce').sum()

            social_behavior_percentage = (social_behavior_sum/(social_behavior_sum + nonsocial_behavior_sum))*100

            individual_behavior["social_behavior"] = social_behavior_sum
            individual_behavior["nonsocial_behavior"] = nonsocial_behavior_sum
            individual_behavior["social_behavior_percentage"] = social_behavior_percentage

            individual_behaviors.append(individual_behavior)
        except:
            print("Exception for participant Id: ", name)
    return individual_behaviors

def generate_behavior_report(individual_behaviors):
    # Get the fieldnames from the first dictionary
    fieldnames = individual_behaviors[0].keys()

    # Open a CSV file for writing
    with open('behavior_report_ehtesham.csv', 'w', newline='') as csvfile:
        # Create a writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for row in individual_behaviors:
            writer.writerow(row)

    print("CSV file has been created successfully.")

sheets_dict = pd.read_excel('coding_ehtesham_1.xlsx', sheet_name=None)
individual_behaviors = calculate_behavior(sheets_dict)    
generate_behavior_report(individual_behaviors)