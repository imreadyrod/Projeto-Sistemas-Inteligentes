import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

## drop de colunas
base = pd.read_csv("../data/base.csv")
base.drop(["Unnamed: 0", "name_team", "name_player", "team_salary", "all_star_appearances"], axis=1, inplace=True)

## encoder da position
positions = base["position"].unique()
le = preprocessing.LabelEncoder()
le.fit(positions)
base["position"] = le.transform(base["position"])

## normalizacao 
def normalize(serie):
    norm = lambda x: (x - serie.min() ) / (serie.max()  - serie.min() )
    return serie.apply(norm)

for x in ["age", "weight", "height", "pts", "ast", "reb"]:
    base[x] = normalize(base[x])

base.to_csv("../data/norm.csv")