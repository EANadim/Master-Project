# Master project



## Installation

First create a virtual environment and activate the virtual environment

Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages

```bash
pip install -r requirements.py
```

## Generate Behavior report

To generate the behavior report you have to put raw coding files of two individual coders in this directory. The names of the files should be `coding_ehtesham.xlsx` & `coding_usman.xlsx` .

Then you run 

```bash
python behavior_report_generator.py
```

This command will generate two behavior reports for each coder: `behavior_report_ehtesham.csv` and `behavior_report_usman.csv`. Each behavior report will include scores for social behavior, non-social behavior, and the percentage of social behavior for each participant.

## Interrater reliability

To measure the interrater reliability if two coders run

```bash
python interrater_reliability_measure.py
```
The command will also print the inter-rater reliability measure for the percentage of social behavior using Pearson correlation along with the corresponding p-value. Additionally, it will generate Cohen's Kappa for sitting distance and angle based on the robot condition.

Moreover, a file named `ranked_social_behavior_deviation.csv` will be created, containing the ranked deviations of social behaviors for each participant according to each coder.


## Descriptive analysis
```bash
python descriptive_analysis.py
```

This command will provide the descriptive analysis of all four conditions.

