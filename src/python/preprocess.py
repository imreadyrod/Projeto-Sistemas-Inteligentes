import pandas as pd
from datetime import date

# # Importando arquivos csv
# # # Citar motivos pelos quais selecionamos apenas essas tabelas
pl_atribute = pd.read_csv("../data/Player_Attributes.csv")
draf_combine = pd.read_csv("../data/Draft_Combine.csv")
pl_salario = pd.read_csv("../data/Player_Salary.csv")
tm_salario = pd.read_csv("../data/Team_Salary.csv")

# # Filtrando apenas a temporada de 2020-21
# # # Selecionamos apenas a temporada de 2020-21 pelo fato de ser 
# # # a temporada mais completa em relacao a disponibilidade de dados
# # # os outros anos estao incompletos ou nao possuem dados sobre todos jogadores
jogadores_temp202021 = pl_salario[(pl_salario.slugSeason =='2020-21')]

# # Convertendo aniversario para datetime
# # # Convertemos para datetime para podermos acessar a data
# # # de maneira mais facil pelos atributos do datetime
pl_atribute["BIRTHDATE"] = pd.to_datetime(pl_atribute["BIRTHDATE"])

# # Merge da tablema de salario de hogadores e seus atributos
# # # Mergeamos essas tabelas no intuito de combinar as informações
# # # que julgamos relevantes para apontar o salario dos jogadores 
# # # e ja ter uma tabela inicial para preprocessarmos 
df = pd.merge(jogadores_temp202021,pl_atribute,left_on = 'namePlayer',right_on = 'DISPLAY_FIRST_LAST',how='inner')

# # Colunas que iremos usar
# # # essas sao as colunas relevantes 
columns = [
    "nameTeam",
    "namePlayer",
    "value",
    "ID",
    "BIRTHDATE",
    "HEIGHT",
    "WEIGHT",
    "POSITION",
    "DRAFT_ROUND",
    "PTS",
    "AST",
    "REB",
    "ALL_STAR_APPEARANCES"
]

df = df[columns]

# # Colunas com campos faltantes
# # # encontramos as colunas com campos faltantes para aplicar o devido
# # # tratamendo indivudualmente
missing = df.isna().sum()
missing = missing[missing > 0]

# # Preenchendo valores nulos
# # # para essa coluna de aparicoes preenchemos com 0 os valores que antes 
# # # eram NaN
df.ALL_STAR_APPEARANCES = df.ALL_STAR_APPEARANCES.fillna(0)

# #  Convertendo aniversario para idade
# # # funcao que utiliza do fato de termos convertido o aniversario para
# # # datetime para calcular a idade. Recebendo a data e retornando a idade 
today = date.today()
def getAge(birthday):
    return today.year - birthday.year - ((today.month,
                                          today.day) < (birthday.month,
                                                        birthday.day))
# # Aplicando funcao
df.BIRTHDATE = df.BIRTHDATE.map(lambda x: getAge(x))

# # Convertendo jogadores undrafteds para 0 
# # # Jogadores que nao tinham sido draftados recebiam o valor de undrafted ou None
# # # substituimos por 0.
df.DRAFT_ROUND[df.DRAFT_ROUND.isin(["Undrafted", "None"])] = 0

# # Removendo salario dos anos nao usados
# # # partindo do principio que usaremos apenas o periodo com maior cobertura de dados
# # # selecionamos o nome do time e os periodos com maior preenchimento do salario
# # # no caso 2020 ate 2022 e fizemos a media desses anos convertendo para uma so coluna
# # # value e dropando as outras  
tm_salario = tm_salario[["nameTeam", "X2020-21", "X2021-22"]]
tm_salario["value"] = (tm_salario["X2020-21"] + tm_salario["X2021-22"]) / 2
tm_salario.drop(["X2020-21", "X2021-22"], inplace=True, axis=1)

# # Convertendo para dicionario 
# # # convertendo o dataframe de salario dos times para um dicionario, contendo a chave 
# # # nome do time e valor salario do time, para facilitar 
# # # a criacao da coluna salario do time no dataframe principal. 
dic = {}
for x in tm_salario.values:
    key = x[0]
    value = x[1]
    dic[key] = value

tm_salario = dic

# # Adicionando coluna salario do time
# # # percorrendo o nome do time para cada jogador e buscando no dicionario o respectivo time
# # # para adicionar a uma nova coluna team_salary no dataframe base 
df["team_salary"] = [tm_salario[x] for x in df["nameTeam"]]

# # Renomeando colunas
# # # renomeando e ordenando as colunas de forma semantica
df.rename(columns={"BIRTHDATE": "age", "namePlayer": "name_player", "nameTeam": "name_team"}, inplace=True)
print(df.columns)
df.columns = df.columns.str.lower()
df = df[['id', 'name_player', 'name_team', 'age', 'height',
       'weight', 'position', 'draft_round', 'pts', 'ast', 'reb',
       'all_star_appearances', 'team_salary', 'value']]

print(df.columns)
# # # Convertendo para csv
df.to_csv("../data/base.csv")