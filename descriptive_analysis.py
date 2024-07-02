import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_descriptive_analysis(behavior_report_name, coder_name):
    df = pd.read_csv(behavior_report_name)

    human_mismatched_data = df[(df['fitting_status'] == 'Mismatch') & (df['target_of_interaction'] == 'Human')]
    human_matched_data = df[(df['fitting_status'] == 'Match') & (df['target_of_interaction'] == 'Human')]
    robot_mismatched_data = df[(df['fitting_status'] == 'Mismatch') & (df['target_of_interaction'] == 'Robot')]
    robot_matched_data = df[(df['fitting_status'] == 'Match') & (df['target_of_interaction'] == 'Robot')]

    print("The descriptive data for coder "+coder_name+" is as follows: ")

    print("Human mismatch condtion social behavior percentage descriptive analysis: ")
    print(human_mismatched_data['social_behavior_percentage'].describe())

    print("Human match condtion social behavior percentage descriptive analysis: ")
    print(human_matched_data['social_behavior_percentage'].describe())

    print("Robot mismatch condtion social behavior percentage descriptive analysis: ")
    print(robot_mismatched_data['social_behavior_percentage'].describe())

    print("Robot match condtion social behavior percentage descriptive analysis: ")
    print(robot_matched_data['social_behavior_percentage'].describe())


    # Set the aesthetic style of the plots
    sns.set_theme(style="whitegrid")

    # Plot histograms
    plt.figure(figsize=(14, 10))

    # Human mismatch condition
    plt.subplot(2, 2, 1)
    sns.histplot(human_mismatched_data['social_behavior_percentage'], bins=20, kde=True, color='blue')
    plt.title('Human Mismatch Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)

    # Human match condition
    plt.subplot(2, 2, 2)
    sns.histplot(human_matched_data['social_behavior_percentage'], bins=20, kde=True, color='green')
    plt.title('Human Match Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)

    # Robot mismatch condition
    plt.subplot(2, 2, 3)
    sns.histplot(robot_mismatched_data['social_behavior_percentage'], bins=20, kde=True, color='red')
    plt.title('Robot Mismatch Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)

    # Robot match condition
    plt.subplot(2, 2, 4)
    sns.histplot(robot_matched_data['social_behavior_percentage'], bins=20, kde=True, color='purple')
    plt.title('Robot Match Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)

    plt.suptitle('Social Behavior Percentage Across Human and Robot Conditions(coder: '+coder_name+')', fontsize=20)

    plt.tight_layout()
    plt.show()

coder_name_1 = "Ehtesham"
behavior_report_name_1 = "behavior_report_ehtesham.csv"
coder_name_2 = "Usman"
behavior_report_name_2 = "behavior_report_usman.csv"

generate_descriptive_analysis(behavior_report_name_1, coder_name_1)
generate_descriptive_analysis(behavior_report_name_2, coder_name_2)
