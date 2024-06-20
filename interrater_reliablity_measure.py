import pandas as pd
import csv
import numpy as np

from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score

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

def generate_behavior_report(individual_behaviors, file_name):
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

def generate_interrater_reliablity_social_behavior_percentage(e_dict, u_dict):
    
    # Select the first and sixth column from the given dataframes
    e_social_behavior_percentage = e_dict.iloc[:, [0, 6]]
    u_social_behavior_percentage = u_dict.iloc[:, [0, 6]]

    # Merge the DataFrames on participant_id
    merged_sbp_df = pd.merge(e_social_behavior_percentage, u_social_behavior_percentage, on='participant_id', suffixes=('_e', '_u'))

    # Check for NaN or infinite values and drop corresponding rows
    merged_sbp_df = merged_sbp_df.replace([np.inf, -np.inf], np.nan).dropna()

    # Extract the cleaned columns again
    e_values_cleaned = merged_sbp_df['social_behavior_percentage_e']
    u_values_cleaned = merged_sbp_df['social_behavior_percentage_u']

    # Calculate Pearson correlation using scipy
    correlation, p_value = pearsonr(e_values_cleaned, u_values_cleaned)

    print("Interrater reliablity for social behavior percentage: ")
    print(f'Pearson correlation: {correlation}')
    print(f'p-value: {p_value}')

    generate_deviation_rank(merged_sbp_df)

def generate_deviation_rank(df): 
    df['deviation'] = abs(df['social_behavior_percentage_e'] - df['social_behavior_percentage_u'])
    ranked_df = df.sort_values(by='deviation', ascending=False).reset_index(drop=True)
    ranked_df[['participant_id', 'social_behavior_percentage_e', 'social_behavior_percentage_u', 'deviation']].to_csv('ranked_social_behavior_deviation.csv', index=False)


def generate_interrater_reliablity_sitting_distance(e_dict, u_dict):
    
    e_sitting_distance = e_dict[e_dict['target_of_interaction'].str.lower() == 'robot']
    u_sitting_distance = u_dict[u_dict['target_of_interaction'].str.lower() == 'robot']

    # Select the first and third column from the given dataframes
    e_sitting_distance = e_sitting_distance.iloc[:, [0, 2]]
    u_sitting_distance = u_sitting_distance.iloc[:, [0, 2]]

    # Merge the DataFrames on participant_id
    merged_sbp_df = pd.merge(e_sitting_distance, u_sitting_distance, on='participant_id', suffixes=('_e', '_u'))

    # Convert to lowercase and replace "middle" with "mid"
    merged_sbp_df['sitting_distance_e'] = merged_sbp_df['sitting_distance_e'].str.lower().replace('middle', 'mid')
    merged_sbp_df['sitting_distance_u'] = merged_sbp_df['sitting_distance_u'].str.lower().replace('middle', 'mid')

    # Extract the cleaned columns
    e_values_cleaned = merged_sbp_df['sitting_distance_e']
    u_values_cleaned = merged_sbp_df['sitting_distance_u']

    # Calculate Cohen's Kappa
    kappa = cohen_kappa_score(e_values_cleaned, u_values_cleaned)
    print(f"Cohen's Kappa for sitting distance in terms of robot: {kappa}")

def generate_interrater_reliablity_sitting_angle(e_dict, u_dict):

    e_sitting_angle = e_dict[e_dict['target_of_interaction'].str.lower() == 'robot']
    u_sitting_angle = u_dict[u_dict['target_of_interaction'].str.lower() == 'robot']

    # Select the first and third column from the given dataframes
    e_sitting_angle = e_sitting_angle.iloc[:, [0, 3]]
    u_sitting_angle = u_sitting_angle.iloc[:, [0, 3]]

    # Merge the DataFrames on participant_id
    merged_sbp_df = pd.merge(e_sitting_angle, u_sitting_angle, on='participant_id', suffixes=('_e', '_u'))

    # Convert to lowercase and replace "45 degrees" with "45 degree"
    merged_sbp_df['sitting_angle_e'] = merged_sbp_df['sitting_angle_e'].str.lower().replace('45 degrees', '45 degree')
    merged_sbp_df['sitting_angle_u'] = merged_sbp_df['sitting_angle_u'].str.lower().replace('45 degrees', '45 degree')

    # Extract the cleaned columns
    e_values_cleaned = merged_sbp_df['sitting_angle_e']
    u_values_cleaned = merged_sbp_df['sitting_angle_u']
    
    # Calculate Cohen's Kappa
    kappa = cohen_kappa_score(e_values_cleaned, u_values_cleaned)
    print(f"Cohen's Kappa for sitting angle in terms of robot: {kappa}")

coding_sheet_name_1 = "coding_ehtesham.xlsx"
coding_sheet_name_2 = "coding_usman.xlsx"

behavior_report_name_1 = "behavior_report_ehtesham.csv"
behavior_report_name_2 = "behavior_report_usman.csv"

# generate behavior report coded by coder 1: Ehtesham
sheets_dict_e = pd.read_excel(coding_sheet_name_1, sheet_name=None)
individual_behaviors_e = calculate_behavior(sheets_dict_e)    
generate_behavior_report(individual_behaviors_e, behavior_report_name_1)

# generate behavior report coded by coder 2: Usman
sheets_dict_u = pd.read_excel(coding_sheet_name_2, sheet_name=None)
individual_behaviors_u = calculate_behavior(sheets_dict_u)    
generate_behavior_report(individual_behaviors_u, behavior_report_name_2)

e_dict = pd.read_csv(behavior_report_name_1)
u_dict = pd.read_csv(behavior_report_name_2)

generate_interrater_reliablity_social_behavior_percentage(e_dict, u_dict)
generate_interrater_reliablity_sitting_distance(e_dict, u_dict)
generate_interrater_reliablity_sitting_angle(e_dict, u_dict)