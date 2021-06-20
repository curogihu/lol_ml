# expect elasepd time with using kill and death amount, and random forest

import json
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from glob import glob
from tqdm import tqdm


def main(input_filename: str, json_paths: list) -> None:
    data = []
    
    for json_path in tqdm(json_paths):
        with open(json_path) as f:
            json_data = json.load(f)

        team_1_kills , team_2_kills = 0, 0
        team_1_deaths , team_2_deaths = 0, 0
        team_1_assits , team_2_assits = 0, 0
        team_1_result , team_2_result = 0, 0

        duration_time = json_data['gameDuration']

        for team in json_data['teams']:
            if team['teamId'] == 100:
                team_1_result = 1 if team['win'] == 'Win' else 0

            else:
                team_2_result = 1 if team['win'] == 'Win' else 0

        for participant in json_data['participants']:
            kills = participant['stats']['kills']
            deaths = participant['stats']['deaths']
            assists = participant['stats']['assists']

            if participant['teamId'] == 100:
                team_1_kills += kills
                team_1_deaths += deaths
                team_1_assits += assists

            else:
                team_2_kills += kills
                team_2_deaths += deaths
                team_2_assits += assists

        extracted_data = [
            duration_time,
            team_1_result, team_1_kills, team_1_deaths, team_1_assits,
            team_2_result, team_2_kills, team_2_deaths, team_2_assits,
        ]

        data.append(extracted_data)

    header_str = 'duration_time,team_1_result,team_1_kills,team_1_deaths,team_1_assits,team_2_result,team_2_kills,team_2_deaths,team_2_assits'
    np.savetxt(input_filename, data, header=header_str, delimiter =",",fmt ='%d', comments='')


def train_randomforest(input_filename: str) -> None:
    df = pd.read_csv(input_filename)

    # print(df.shape)
    # print(df.head())

    y = df['duration_time']

    df_data = df.drop(['duration_time', 'team_1_result', 'team_2_result'], axis=1)
    X = df_data.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    clf = RandomForestClassifier(random_state=1234)
    clf.fit(X_train, y_train)

    # print("score=", clf.score(X_test, y_test))

    y_pred = clf.predict(X_test)

    accu = accuracy_score(y_test, y_pred)
    print('accuracy = {:>.4f}'.format(accu))

    # # Feature Importance
    # fti = clf.feature_importances_   

    # print('Feature Importances:')
    # for i in range(8):
    #     # print('\t{0:20s} : {1:>.6f}'.format(feat, fti[i]))
    #     print(fti[i])

    



if __name__ == '__main__':
    input_filename = 'result.csv'
    # json_files = sorted(glob('D:\output\game\info\\*.json'))

    # result_data = main(input_filename, json_files)

    train_randomforest(input_filename)

    

    # print(len(result))

    # try_random_forest(result_data)