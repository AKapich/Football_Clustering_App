import pandas as pd
import numpy as np

play_patterns_dict = {
    'Goalkeeper': 2,
    'Full Back': 3,
    'Centre Back': 3,
    'Defensive Midfielder': 4,
    'Central Midfielder': 4,
    'Attacking Midfielder': 2,
    'Winger': 3,
    'Centre Forward': 3
}


position_name_dict = {
    'Goalkeeper': ['Goalkeeper'],
    'Full Back': ['Right-Back', 'Left-Back'],
    'Centre Back': ['Centre-Back'],
    'Defensive Midfielder': ['Defensive Midfield'],
    'Central Midfielder': ['Central Midfield'],
    'Attacking Midfielder': ['Attacking Midfield', 'Second Striker'],
    'Winger': ['Left Winger', 'Right Winger', 'Left Midfield', 'Right Midfield'],
    'Centre Forward': ['Centre-Forward']
}



relevant_features_dict = {
    'Goalkeeper': 
            ["Clean Sheet Percentage",
            "PSxG-GA",
            "Pass Completion Percentage (Launched)",
            "Passes Attempted",
            "Throws Attempted",
            "Launch %",
            "Average Pass Length",
            "Launch% (Goal Kicks)",
            "Avg. Length of Goal Kicks",
            "Crosses Stopped %",
            "Def. Actions Outside Pen. Area",
            "Avg. Distance of Def. Actions"],
    'Full Back':
            ["Assists",
            "xAG",
            "Expected Assists",
            "Progressive Carries",
            "Progressive Passes",
            "Progressive Passes Rec",
            "Key Passes",
            "Passes into Final Third",
            "Passes into Penalty Area",
            "Crosses into Penalty Area",
            "Pass Completion %",
            "Passes Attempted",
            #"Total Passing Distance",
            "Progressive Passing Distance",
            "Through Balls",
            "Crosses",
            "Shot-Creating Actions",
            "SCA (TO)",
            "Tackles",
            "Tackles Won",
            "Tackles (Def 3rd)",
            "Tackles (Mid 3rd)",
            "Tackles (Att 3rd)",
            "% of dribblers tackled",
            "Clearances",
            "Errors",
            "Touches (Def Pen)",
            "Touches (Def 3rd)",
            "Touches (Mid 3rd)",
            "Touches (Att 3rd)",
            "Touches (Att Pen)",
            "Take-Ons Attempted",
            "Successful Take-On %",
            #"Total Carrying Distance",
            "Progressive Carrying Distance",
            "Progressive Carries",
            "Carries into Final Third",
            "Carries into Penalty Area"],
    'Centre Back':
            ["Progressive Carries",
            "Progressive Passes",
            "Pass Completion %",
            "Passes Attempted",
            #"Total Passing Distance",
            "Progressive Passing Distance",
            "Passes into Final Third",
            "Through Balls",
            "Crosses",
            "Tackles",
            "Tackles Won",
            "Tackles (Def 3rd)",
            "Tackles (Mid 3rd)",
            "Tackles (Att 3rd)",
            "% of dribblers tackled",
            "Blocks",
            "Shots Blocked",
            "Rival Passes Blocked",
            "Tkl+Int",
            "Clearances",
            "Errors",
            "Touches (Def 3rd)",
            "Touches (Mid 3rd)",
            "Touches (Att 3rd)",
            #"Total Carrying Distance",
            "Progressive Carrying Distance",
            "Carries into Final Third",
            "Miscontrols",
            "Ball Recoveries",
            "Aerials won",
            "Aerials lost",
            "% of Aerials Won"],
    'Defensive Midfielder':
            ["Successful Take-Ons",
            "Progressive Carries",
            "Progressive Passes",
            "Pass Completion %",
            "Passes Attempted",
            #"Total Passing Distance",
            "Progressive Passing Distance",
            "Passes into Final Third",
            "Passes into Penalty Area",
            "Crosses into Penalty Area",
            "Through Balls",
            "Tackles Won",
            "Tackles (Def 3rd)",
            "Tackles (Mid 3rd)",
            "Tackles (Att 3rd)",
            "% of dribblers tackled",
            "Touches (Def 3rd)",
            "Touches (Mid 3rd)",
            "Touches (Att 3rd)",
            #"Total Carrying Distance",
            "Progressive Carrying Distance",
            "Carries into Final Third",
            'Ball Recoveries',
            "Aerials won",
            "% of Aerials Won"],
    'Central Midfielder':
            ["Assists",
            "xAG",
            "Progressive Carries",
            "Progressive Passes",
            "Progressive Passes Rec",
            "Shots Total",
            "Average Shot Distance",
            "npxG/Sh",
            "Passes Attempted",
            "Pass Completion %",
            "Progressive Passing Distance",
            "Expected Assists",
            "Key Passes",
            "Passes into Final Third",
            "Passes into Penalty Area",
            "Through Balls",
            "Shot-Creating Actions",
            "Tackles",
            "Successful Take-Ons",
            #"Total Carrying Distance",
            "Progressive Carrying Distance",
            "Carries into Final Third",
            "Carries into Penalty Area",
            "Touches (Def 3rd)",
            "Touches (Mid 3rd)",
            "Touches (Att 3rd)",
            'Passes Offside'],
    'Attacking Midfielder':
            ["Non-Penalty xG",
            "xAG",
            "Progressive Carries",
            "Progressive Passes",
            "Progressive Passes Rec",
            "Shots Total",
            "Shots on target %",
            "Average Shot Distance",
            "npxG/Sh",
            "Non-Penalty Goals - npxG",
            "Pass Completion %",
            "Progressive Passing Distance",
            "Expected Assists",
            "Key Passes",
            "Passes into Penalty Area",
            "Through Balls",
            "Shot-Creating Actions",
            "Goal-Creating Actions",
            "Touches (Def 3rd)",
            "Touches (Mid 3rd)",
            "Touches (Att 3rd)",
            "Touches (Att Pen)",
            "Take-Ons Attempted",
            "Successful Take-On %",
            "Progressive Carrying Distance",
            "Carries into Penalty Area",
            "Penalty Kicks Won"],
    'Winger':
            ["Non-Penalty xG",
            "xAG",
            "Progressive Carries",
            "Progressive Passes",
            "Progressive Passes Rec",
            "Shots Total",
            "Shots on target %",
            "Average Shot Distance",
            "npxG/Sh",
            "Non-Penalty Goals - npxG",
            "Passes Attempted",
            "Pass Completion %",
            "Progressive Passing Distance",
            "Expected Assists",
            "Key Passes",
            "Passes into Final Third",
            "Passes into Penalty Area",
            "Crosses into Penalty Area",
            "Through Balls",
            "Shot-Creating Actions",
            "SCA (TO)",
            "Goal-Creating Actions",
            "GCA (TO)",
            "Touches (Def 3rd)",
            "Touches (Mid 3rd)",
            "Touches (Att 3rd)",
            "Touches (Att Pen)",
            "Successful Take-Ons",
            "Successful Take-On %",
            "Times Tackled During Take-On",
            "Tackled During Take-On Percentage",
            #"Total Carrying Distance",
            "Progressive Carrying Distance",
            "Carries into Final Third",
            "Carries into Penalty Area",
            "Penalty Kicks Won"],
    'Centre Forward':
            ["Non-Penalty xG",
            "xAG",
            "Progressive Passes Rec",
            "Shots Total",
            "Shots on target %",
            "Goals/Shot",
            "Goals/Shot on target",
            "npxG/Sh",
            "Non-Penalty Goals - npxG",
            "Average Shot Distance",
            "Progressive Passing Distance",
            "Passes into Penalty Area",
            "Expected Assists",
            "Key Passes",
            "Shot-Creating Actions",
            "Goal-Creating Actions",
            "Tackles (Att 3rd)",
            "Touches (Mid 3rd)",
            "Touches (Att 3rd)",
            "Touches (Att Pen)",
            "Take-Ons Attempted",
            "Successful Take-On %",
            "Progressive Carrying Distance",
            "Carries into Penalty Area",
            "Offsides",
            "Penalty Kicks Won",
            "Aerials won",
            "% of Aerials Won"]
}

new_metrics_dict = {
    'Goalkeeper': [],
    'Full Back': ['Shots&Passes Blocked', 'Lost Control', 'Progressive Carrries per 100 Touches',
                    'Progressive Passes per 100 Passes', 'xA per Key Pass'],
    'Centre Back': ['Shots&Passes Blocked', 'Progressive Carrries per 100 Touches',
                     'Progressive Passes per 100 Passes', 'Pass Long2Short Ratio'],
    'Defensive Midfielder': ['Shots&Passes Blocked', 'Progressive Carrries per 100 Touches',
                              'Progressive Passes per 100 Passes',  'Pass Long2Short Ratio'],
    'Central Midfielder': ['Progressive Carrries per 100 Touches', 'Progressive Passes per 100 Passes', 'xA per Key Pass',
                            'Pass Long2Short Ratio', 'Key Passes per 100 Passes'],
    'Attacking Midfielder': ['Progressive Carrries per 100 Touches', 'Progressive Passes per 100 Passes',
                              'xA per Key Pass', 'Key Passes per 100 Passes'],
    'Winger': ['Progressive Carrries per 100 Touches', 'Progressive Passes per 100 Passes', 'xA per Key Pass',
                'Key Passes per 100 Passes', 'Lost Control'],
    'Centre Forward': ['xA per Key Pass', 'Key Passes per 100 Passes', 'Lost Control']
}


def calculate_new_metrics(df):
    df['Shots&Passes Blocked'] = df['Shots Blocked'] + df['Rival Passes Blocked'] + df['Interceptions']
    df['Lost Control'] = df['Dispossessed'] + df['Miscontrols']
    df['Progressive Carrries per 100 Touches'] = 100 * df['Progressive Carries'] / df['Touches']
    df['Progressive Passes per 100 Passes'] = 100 * df['Progressive Passes'] / df['Passes Attempted']
    df['xA per Key Pass'] = df['Expected Assists'] / df['Key Passes']
    df['Pass Long2Short Ratio'] = df['Passes Completed (Long)'] / df['Passes Completed (Short)']
    df['Key Passes per 100 Passes'] = 100 * df['Key Passes'] / df['Passes Attempted']
    df['Lost Control'] = df['Dispossessed'] + df['Miscontrols']


def process(df, position):
    df = df[df['DetailedPosition'].isin(position_name_dict[position])]
    
    if position != 'Goalkeeper':
        calculate_new_metrics(df)
        df.replace([np.inf, -np.inf], 0, inplace=True)

    columns = relevant_features_dict[position] + new_metrics_dict[position]
    
    df = df[columns]
    perc_columns = df.select_dtypes(include=['object']).columns
    df[perc_columns] = df[perc_columns].applymap(lambda x: float(str(x).replace('%', '')))

    return df
