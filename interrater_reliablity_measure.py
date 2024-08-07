import pandas as pd
import numpy as np

from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score

def generate_interrater_reliablity_social_behavior_percentage(e_dict, u_dict):
    """Generates behavior report which is calculated by calculate_behavior function & then saves as the provided file name"""

    # Select the first and sixth column from the given dataframes
    e_social_behavior_percentage = e_dict.iloc[:, [0, 7]]
    u_social_behavior_percentage = u_dict.iloc[:, [0, 7]]

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
    """A file named `ranked_social_behavior_deviation.csv` will be created, containing the ranked deviations of social behaviors for each participant according to each coder."""

    df['deviation'] = abs(df['social_behavior_percentage_e'] - df['social_behavior_percentage_u'])
    ranked_df = df.sort_values(by='deviation', ascending=False).reset_index(drop=True)
    ranked_df[['participant_id', 'social_behavior_percentage_e', 'social_behavior_percentage_u', 'deviation']].to_csv('ranked_social_behavior_deviation.csv', index=False)


def generate_interrater_reliablity_sitting_distance(e_dict, u_dict):
    """Generate Cohen's Kappa for sitting distance in robot condition"""

    e_sitting_distance = e_dict[e_dict['target_of_interaction'].str.lower() == 'robot']
    u_sitting_distance = u_dict[u_dict['target_of_interaction'].str.lower() == 'robot']

    # Select the first and third column from the given dataframes
    e_sitting_distance = e_sitting_distance.iloc[:, [0, 3]]
    u_sitting_distance = u_sitting_distance.iloc[:, [0, 3]]

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
    """Generate Cohen's Kappa for sitting angle in robot condition"""

    e_sitting_angle = e_dict[e_dict['target_of_interaction'].str.lower() == 'robot']
    u_sitting_angle = u_dict[u_dict['target_of_interaction'].str.lower() == 'robot']

    # Select the first and third column from the given dataframes
    e_sitting_angle = e_sitting_angle.iloc[:, [0, 4]]
    u_sitting_angle = u_sitting_angle.iloc[:, [0, 4]]

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


# The generated behavior report files will have these correspondent names
behavior_report_name_1 = "./behavior_report/behavior_report_ehtesham.csv"
behavior_report_name_2 = "./behavior_report/behavior_report_usman.csv"

e_dict = pd.read_csv(behavior_report_name_1)
u_dict = pd.read_csv(behavior_report_name_2)

generate_interrater_reliablity_social_behavior_percentage(e_dict, u_dict)
generate_interrater_reliablity_sitting_distance(e_dict, u_dict)
generate_interrater_reliablity_sitting_angle(e_dict, u_dict)