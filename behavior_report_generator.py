import pandas as pd
import csv

def calculate_behavior(sheets_dict):
    """Calculates the total social behavior, non-social behavior & social behavior percentage score"""

    data_conditions_dict = pd.read_excel("data_conditions.xlsx")
    individual_behaviors = []
    for  name, df_sheet in sheets_dict.items():
        try:
            individual_behavior = {}
            
            individual_behavior["participant_id"] = name
            
            fitting_status = data_conditions_dict.loc[data_conditions_dict['Code'].str.lower() == name.lower(), "Match/Mismatch"]
            if not fitting_status.empty:
                individual_behavior["fitting_status"] = fitting_status.values[0]
            else:
                individual_behavior["fitting_status"] = ""

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

            moving_col = df_sheet.iloc[:, 8]
            laughing_col = df_sheet.iloc[:, 9]
            gazing_col = df_sheet.iloc[:, 10]
            talking_col = df_sheet.iloc[:, 11]
            touching_col = df_sheet.iloc[:, 12]
            other_col = df_sheet.iloc[:, 13]

            moving_score_sum = pd.to_numeric(moving_col, errors='coerce').sum()
            laughing_score_sum = pd.to_numeric(laughing_col, errors='coerce').sum()
            gazing_score_sum = pd.to_numeric(gazing_col, errors='coerce').sum()
            talking_score_sum = pd.to_numeric(talking_col, errors='coerce').sum()
            touching_score_sum = pd.to_numeric(touching_col, errors='coerce').sum()
            other_score_sum = pd.to_numeric(other_col, errors='coerce').sum()

            total_behavior_sum = social_behavior_sum + nonsocial_behavior_sum

            moving_score_percentage = (moving_score_sum/total_behavior_sum)*100
            laughing_score_percentage = (laughing_score_sum/total_behavior_sum)*100
            gazing_score_percentage = (gazing_score_sum/total_behavior_sum)*100
            talking_score_percentage = (talking_score_sum/total_behavior_sum)*100
            touching_score_percentage = (touching_score_sum/total_behavior_sum)*100
            other_score_percentage = (other_score_sum/total_behavior_sum)*100

            individual_behavior["moving_score_percentage"] = moving_score_percentage
            individual_behavior["laughing_score_percentage"] = laughing_score_percentage
            individual_behavior["gazing_score_percentage"] = gazing_score_percentage
            individual_behavior["talking_score_percentage"] = talking_score_percentage
            individual_behavior["touching_score_percentage"] = touching_score_percentage
            individual_behavior["other_score_percentage"] = other_score_percentage

            individual_behaviors.append(individual_behavior)
        except:
            print("Exception for participant Id: ", name)
    return individual_behaviors

def generate_behavior_report(individual_behaviors, file_name):
    """Generates behavior report which is calculated by calculate_behavior function & then saves as the provided file name"""

    # Get the fieldnames from the first dictionary
    fieldnames = individual_behaviors[0].keys()

    # Open a CSV file for writing
    with open(file_name, 'w', newline='') as csvfile:
        # Create a writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for row in individual_behaviors:
            writer.writerow(row)

    print("CSV file has been created successfully.")


# These coding sheets with the correspondent names should be present in this directory while running this script
coding_sheet_name_1 = "./coding_archive/latest/coding_ehtesham.xlsx"
coding_sheet_name_2 = "./coding_archive/latest/coding_usman.xlsx"

# The generated behavior report files will have these correspondent names
behavior_report_name_1 = "./behavior_report/behavior_report_ehtesham.csv"
behavior_report_name_2 = "./behavior_report/behavior_report_usman.csv"

# generate behavior report coded by coder 1: Ehtesham
sheets_dict_e = pd.read_excel(coding_sheet_name_1, sheet_name=None)
individual_behaviors_e = calculate_behavior(sheets_dict_e)    
generate_behavior_report(individual_behaviors_e, behavior_report_name_1)

# generate behavior report coded by coder 2: Usman
sheets_dict_u = pd.read_excel(coding_sheet_name_2, sheet_name=None)
individual_behaviors_u = calculate_behavior(sheets_dict_u)    
generate_behavior_report(individual_behaviors_u, behavior_report_name_2)