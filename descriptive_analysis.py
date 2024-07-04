import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar_chart(human_mismatched_data, human_matched_data, robot_mismatched_data, robot_matched_data, coder_name):
    # Function to set the y-axis limit
    def set_axis_lim(ax):
        ax.set_xlim(0, 100)
        y_min, y_max = ax.get_ylim()
        if y_max < 7:
            ax.set_ylim(0, 7)


    # Set the aesthetic style of the plots
    sns.set_theme(style="whitegrid")

    # Plot histograms
    plt.figure(figsize=(14, 10))

    # Human mismatch condition
    ax1 = plt.subplot(2, 2, 1)
    sns.histplot(human_mismatched_data['social_behavior_percentage'], bins=20, kde=True, color='blue')
    plt.title('Human Mismatch Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Number of participants', fontsize=14)
    plt.grid(True)
    set_axis_lim(ax1)

    # Human match condition
    ax2 = plt.subplot(2, 2, 2)
    sns.histplot(human_matched_data['social_behavior_percentage'], bins=20, kde=True, color='green')
    plt.title('Human Match Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Number of participants', fontsize=14)
    plt.grid(True)
    set_axis_lim(ax2)

    # Robot mismatch condition
    ax3 = plt.subplot(2, 2, 3)
    sns.histplot(robot_mismatched_data['social_behavior_percentage'], bins=20, kde=True, color='red')
    plt.title('Robot Mismatch Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Number of participants', fontsize=14)
    plt.grid(True)
    set_axis_lim(ax3)

    # Robot match condition
    ax4 = plt.subplot(2, 2, 4)
    sns.histplot(robot_matched_data['social_behavior_percentage'], bins=20, kde=True, color='purple')
    plt.title('Robot Match Condition', fontsize=16)
    plt.xlabel('Social Behavior Percentage', fontsize=14)
    plt.ylabel('Number of participants', fontsize=14)
    plt.grid(True)
    set_axis_lim(ax4)

    plt.suptitle('Social Behavior Percentage Across Human and Robot Conditions (coder: '+coder_name+')', fontsize=20)

    plt.tight_layout()
    plt.show()

def plot_box_plot(human_mismatched_data, human_matched_data, robot_mismatched_data, robot_matched_data, coder_name):
    # Combine data into a single DataFrame
    data = pd.DataFrame({
        'Human Mismatched': human_mismatched_data['social_behavior_percentage'],
        'Human Matched': human_matched_data['social_behavior_percentage'],
        'Robot Mismatched': robot_mismatched_data['social_behavior_percentage'],
        'Robot Matched': robot_matched_data['social_behavior_percentage']
    })

    # Melt the DataFrame to long format
    data_melted = data.melt(var_name='Condition', value_name='Social Behavior Percentage')

    # Create the boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Condition', y='Social Behavior Percentage', data=data_melted)

    # Overlay the stripplot with specific colors
    palette = ['blue', 'green', 'red', 'purple']
    sns.stripplot(x='Condition', y='Social Behavior Percentage', data=data_melted, 
                jitter=True, palette=palette, alpha=0.5)

    plt.title('Boxplot of Social Behavior Percentages across different conditions (Coder: '+ coder_name+')')
    plt.xlabel('Condition')
    plt.ylabel('Social Behavior Percentage')
    plt.show()
    
def generate_descriptive_analysis(behavior_report_name, coder_name):
    df = pd.read_csv(behavior_report_name)

    human_mismatched_data = df[(df['fitting_status'] == 'Mismatch') & (df['target_of_interaction'] == 'Human')]
    human_matched_data = df[(df['fitting_status'] == 'Match') & (df['target_of_interaction'] == 'Human')]
    robot_mismatched_data = df[(df['fitting_status'] == 'Mismatch') & (df['target_of_interaction'] == 'Robot')]
    robot_matched_data = df[(df['fitting_status'] == 'Match') & (df['target_of_interaction'] == 'Robot')]

    print("The descriptive data for coder "+coder_name+" is as follows: ")

    print("Human mismatch condition social behavior percentage descriptive analysis: ")
    print(human_mismatched_data['social_behavior_percentage'].describe())

    print("Human match condition social behavior percentage descriptive analysis: ")
    print(human_matched_data['social_behavior_percentage'].describe())

    print("Robot mismatch condition social behavior percentage descriptive analysis: ")
    print(robot_mismatched_data['social_behavior_percentage'].describe())

    print("Robot match condition social behavior percentage descriptive analysis: ")
    print(robot_matched_data['social_behavior_percentage'].describe())

    plot_bar_chart(human_mismatched_data, human_matched_data, robot_mismatched_data, robot_matched_data, coder_name)
    plot_box_plot(human_mismatched_data, human_matched_data, robot_mismatched_data, robot_matched_data, coder_name)

coder_name_1 = "Ehtesham"
behavior_report_name_1 = "./behavior_report/behavior_report_ehtesham.csv"
coder_name_2 = "Usman"
behavior_report_name_2 = "./behavior_report/behavior_report_usman.csv"

generate_descriptive_analysis(behavior_report_name_1, coder_name_1)
generate_descriptive_analysis(behavior_report_name_2, coder_name_2)
