# NBA

**Caio Felix Reis, 1429187@sga.pucminas.br**

**Pedro Henrique Rodrigues da Silva, pedro.silva1429338@sga.pucminas.br**

**Lucas Rocha Van Huysse, lhuysse@sga.pucminas.br**

**Rodrigo de Oliveira Santos,  rodrigo.santos.1428766@sga.pucminas.br**

---

Professores:

** Prof. Nome do Prof 1 **
** Prof. Nome do Prof 2 **

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---


## Introdução

A NBA é uma das maiores ligas esportivas do mundo e todos os anos movimenta milhões de dólares em patrocínios. Além do dinheiro envolvido, existe uma infinidade de métricas sobre jogadores e equipes, sendo uma grande oportunidade para apaixonados por dados. 
Tendo como fonte a API do “stats.nba.com”, nossos sensores disponibilizarão dados de mais de 60.000 jogos contendo todos os aspectos da NBA, considerando os times, jogadores, notícias, drafts, salários, entre outros. Do outro lado, o agente atuador será nosso modelo, que a partir das características fornecidas pelos sensores, filtrará apenas os dados relevantes para a predição do salário do jogador, no ano presente. 
Deste modo, esperamos obter uma resposta racional e potencialmente assertiva na definição do possível salário do jogador.

###    Contextualização

O basquete é um esporte complexo onde atributos físicos, performance fisiológica, atributos técnicos, conhecimento tático e atributos fisiológicos contribuem para o jogador e a para o sucesso em geral da equipe. Desta maneira, determinar um possivel salário para um determinado jogador é uma tarefa difícil.  
Em relação ao basquete, os atributos físicos a performance fisiológica são características determinantes no sucesso do atleta (TORRES-UNDA, 2013).  Essas características podem ser traduzidas em capacidade de antecipação do jogador, que refletem nas variáveis relacionadas a pontuação e passes. Ou seja, a capacidade de perceber melhor o ambiente e se adaptar a situação faz com que o jogador tenha um maior desempenho (LORENZO et al.,2019).

###    Problema

Determinar o salário de um jogador na liga da NBA é uma tarefa ardua, devido às suas características de alta pontuação e rápidas flutuações de cenários.
Tendo em vista a alta qualidade times da NBA, os inumeros fatores e adversidades que implicam a qualidade e potencial de um jogador,
é trabalhoso identificar uma possivel salário sem profissionais especificados, oque demanda maior investimento na contratação de um jogador. 

###    Objetivo geral
Prever o possível salário de um jogador.
####    Objetivos específicos
+ Analizar variaveis com maior correlação com o salário de jogadores.  
+ Analizar média de pontos, rebotes e assistências dos jogadores.

###    Justificativas

Auxiliar na parte financeira de cada clube mostrando qual a estimativa ideal de salário para cada jogador baseado em seus dados e características

##    Público alvo

Nosso projeto é indicado para a diretoria de clubes de basquete da NBA.


## Análise exploratórida dos dados

###    Dicionário de dados

Em nossa base, temos várias tabelas que possuem dados detalhados sobre os últimos anos da NBA. Porém tabelas que serão utilizados são:

![2022-12-06 (3)](https://user-images.githubusercontent.com/111394244/206043193-3787083e-778d-4049-8516-0c38aeb8997f.png)


E nossos atributos usados serão:

![2022-12-06 (2)](https://user-images.githubusercontent.com/111394244/206043306-ff88c95b-f54f-4f65-8c95-b625132922e8.png)




###    Descrição de dados
Utilizando da biblioteca pandas e usando o arquivo final 'norm.csv', convertido em um pandas dataframe, podemos descrever os dados estatisticamente através do describe.
![print](https://user-images.githubusercontent.com/64283442/206040667-536e6cbf-bee0-4256-ae58-2578cc010b0a.png)

## Preparação dos dados
Para preparar os dados começamos por dropar os campos que julgamos de não importancia para o modelo.
![image](https://user-images.githubusercontent.com/64283442/206041646-f45b36e7-ebe8-47a1-9105-f0a9ce0e6ddf.png)

Percebemos então a necessidade de rodar um algoritmo de encoding no campo _position_ por ser um campo categórico. Utilizamos o _preprocessing.LabelEncoder_ da biblioteca sklearn.
![image](https://user-images.githubusercontent.com/64283442/206042317-a442cad4-97a2-4511-91b0-3678593db5ed.png)

Normalizamos então as colunas numéricas com o algoritmo de _MinMaxScaler_ dos campos de treino e aplicamos o log10 
no campo _target_ value, por ter uma distribuição cauda longa. 
E finalizamos criando um novo csv com os dados já prontos.
![image](https://user-images.githubusercontent.com/64283442/206043581-fa9727dd-a686-44db-b603-90912f236290.png)

## Indução de modelos

### Modelo 1: Random Forest Regressor
Abaixo segue os tipos de amostragem que foram utilizados no algoritimo.

![2022-12-06 (7)](https://user-images.githubusercontent.com/111394244/206047954-bc4e0abe-6379-47b8-aa3c-e76bf4daef0c.png)

Abaixo segue os parametros usados em nosso modelo.

![2022-12-06 (9)](https://user-images.githubusercontent.com/111394244/206049796-b5aa64f4-3167-4a71-9383-6b454ca0c008.png)

![2022-12-06 (8)](https://user-images.githubusercontent.com/111394244/206050002-cbdb315b-739c-48b7-85d3-49e5695eec77.png)


### Modelo 2: MLP Regressor 
Abaixo segue os tipos de amostragem que foram utilizados no algoritimo.

![2022-12-06 (11)](https://user-images.githubusercontent.com/111394244/206050373-46c511f1-59c7-4d11-aabd-d0b5ef0af28c.png)

Abaixo segue os parametros usados em nosso modelo.

![2022-12-06 (10)](https://user-images.githubusercontent.com/111394244/206050443-a117c599-286b-47b4-be06-e029ab82bead.png)


![2022-12-06 (12)](https://user-images.githubusercontent.com/111394244/206050485-5c26e659-44cc-4d05-8d84-5097bb22946b.png)





## RESULTADOS

## Métricas Utilizadas para Avaliar Modelos de Regressão

O _*sklearn.metrics*_ implementa várias funções de perda, pontuação e utilidade para medir o desempenho da regressão. Abaixo é apresentado um breve resumo das métricas que serão utilizadas para avaliar a regressão


 A _r2_scorefunction_ calcula o coeficiente de determinação , geralmente denotado como:

$$

R^2(y, \hat{y}) = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}

$$

Onde $\hat y$ é o valor predito e $\bar y$ é o valor médio das amostras $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$  

O $R^2$ fornece uma indicação da qualidade do ajuste e, portanto, uma medida de quão bem as amostras não vistas provavelmente serão previstas pelo modelo. A melhor pontuação possível é 1,0 e pode ser negativa (porque o modelo pode ser arbitrariamente pior).

 
Outra métrica muito importante é a  _**MAE**_ (_mean absolut error_):
 $$
 \text{MAE}(y, \hat{y}) = \frac{1}{n_{\text{samples}}} \sum_{i=0}^{n_{\text{samples}}-1} \left| y_i - \hat{y}_i \right|$$

O _MAE_ é simplesmente, como o nome sugere, a média dos erros absolutos. O erro absoluto é o valor absoluto da diferença entre o valor previsto e o valor real. O erro absoluto médio mede a precisão de variáveis contínuas. O _MAE_ nos diz o tamanho médio do erro que podemos esperar da previsão.


O _**MSE**_ (_mean squared error_) erro quadrado médio:

$$\text{MSE}(y, \hat{y}) = \frac{1}{n_\text{samples}} \sum_{i=0}^{n_\text{samples} - 1} (y_i - \hat{y}_i)^2$$

Nos informa o quão perto uma linha de regressão está de um conjunto de pontos de dados. Um MSE maior indica que os pontos de dados estão amplamente dispersos em torno da média, enquanto um MSE menor sugere o contrário. Um MSE menor é preferido porque indica que seus pontos estão mais próximos da média. Ele reflete a distribuição centralizada de seus valores de dados, o fato de não ser distorcido e, o mais importante, ter menos erros (erros medidos pela dispersão dos pontos de dados de sua média).

Menor o MSE => Menor o erro => Melhor o estimador.


O _**MSLE**_ (_mean squared log error_) logaritmo do erro quadrado médio:

$$\text{MSLE}(y, \hat{y}) = \frac{1}{n_\text{samples}} \sum_{i=0}^{n_\text{samples} - 1} (\log_e (1 + y_i) - \log_e (1 + \hat{y}_i) )^2$$

Tem sido uma métrica muito importante apresentada nos modelos de ciência de dados. O seu valor não sofre grandes variações com a presença de outliers, devido à função log imbutida em sua fórmula. Devido as propriedades desta função, o $(\log_e (1 + y_i) - \log_e (1 + \hat{y}_i))$ representa uma  fração dos erros. Ou seja, a escala em que se encontra não é significante, mesmo para valores altos, sempre estaremos no intervalo de 0 e 1. Por último e mais importante, essa métrica sobrecarrega o erro de previsão quando este está abaixo do valor real. Em outras palavras, caso o salário real do jogador for menor do que o valor previsto, o MSLE será pequeno.


O _**MAPE**_ (_mean absolute percentage error_):

$$\text{MAPE}(y, \hat{y}) = \frac{1}{n_{\text{samples}}} \sum_{i=0}^{n_{\text{samples}}-1} \frac{{}\left| y_i - \hat{y}_i \right|}{\max(\epsilon, \left| y_i \right|)}$$

Onde o $\epsilon$ em ${\max(\epsilon, \left| y_i \right|)}$ ocorre para evitar resultados indefinidos quando o $\text y$ é zero.

Este é um dos indicadores mais usados para verificar a acurácia da previsão, por ser de fácil compreensão e interpretação. Essa métrica trata do erro absoluto divido pelo real assim você tem a distância em % do predito em relação ao realizado.


_**MedAE**_ (_median absolute error_):

$$\text{MedAE}(y, \hat{y}) = \text{median}(\mid y_1 - \hat{y}_1 \mid, \ldots, \mid y_n - \hat{y}_n \mid)$$

A melhor maneira de entender o _**MedAE**_ é entender como ele é calculado. Primeiro, é calculado o valor absoluto da distância entre o valor predito e o real, para todas as amostras e então é retirada a mediana desse conjunto de valores. Assim, essa métrica nos retorna o percentil 50 dos erros, desta maneira, conseguimos observar qual a distribuição dos erros 50% acima e 50% abaixo.


A função _**max_error**_ calcula o erro residual máximo , uma métrica que captura o erro de pior caso entre o valor previsto e o valor verdadeiro.

$$\text{Max Error}(y, \hat{y}) = \max(| y_i - \hat{y}_i |)$$





### Resultados obtidos com o Random Forest Regressor 



* Tabela com o valor das métricas utilizadas:

 R² | Erro Absoluto Médio | Erro Quadrático Médio | MSLE(Logaritmo do Erro Quadrático Médio) | MAPE(Percentual do Erro Médio Absoluto) | MedAE(mediana do erro absoluto) | Erro Máximo |
--- |--- |--- |--- |--- |--- |--- |
 0.65| 4.21077e+06 | 3.49325e+13 | 0.988728 | 222,154% | 2.60454e+06 | 1.98524e+07 |



* Tabela com o peso dos atributos:

age | height | weight | position | draft_round | pts | ast | reb |
--- |--- |--- |--- |--- |--- |--- |--- |
0.15 | 0.03 | 0.04 | 0.02 | 0.01 | 0.59 | 0.11 | 0.06 |



### Interpretação do Random Forest Regressor

O modelo obteve R² de 65%, esta é a base para os modelos de regressão pois demonstra a qualidade do ajuste realizado. 
Neste caso, em 100 amostras iriamos conseguir prever ```65%```.

Dentro desses 35% de erro, temos que, em média, de acordo com o MAE, o valor do salário esta defasado de, aproximadamente, ```US$421.077,00```. Essa defasagem pode ser considerada grande, pois o MSE obtido indica  que os valores estão muito dispersos em relação à media. Este dado pode ser corroborado pelo MAPE de ```220%```. 

Dentro do conjunto de avaliações, o nosso modelo está retornando, em média, um ```valor de predição abaixo do salário real que o jogador deveria ganhar```. Informação constatada pelo MSLE. Esta métrica é muito importante, pois, se tratando de dinheiro gasto, teremos uma folga no orçamento caso o regressor seja utilizado.

Por último, podemos ver que a mediana dos erros está em conformidade com os valores já apresentados. o MedAE é de,aproximadamente, ```US$260.454,00``` dólares. Ou seja, 50% dos erros estão abaixo desse valor e 50% estão acima, sendo que, o erro máximo foi de, aproximadamente, ```US$1.985.240,00```. 

Avaliando o peso que o modelo depositou em cada atributo, podemos realizar algumas críticas. De fato, a taxa de pontos que o jogador conquistou é muito importante, porém, as assistências e os rebotes, também possuem seu valor, e nesse caso, o regressor não foi capaz de identificar essa tendência. Outros fatores interessantes são é o peso a altura e a idade dos jogadores. Normalmente, a liga possui uma distribuição uniforme destes atributos.  


### Resultados obtidos com o MLP Regressor

* Tabela com o valor das métricas utilizadas:

 R² | MAE (Erro Absoluto Médio) | MSE (Erro Quadrático Médio) | MSLE(Logaritmo do Erro Quadrático Médio) | MAPE(Percentual do Erro Médio Absoluto) | MedAE (Mediana do Erro Absoluto) | Erro Máximo |
--- |--- |--- |--- |--- |--- |--- |
 -0.65| 8.21302e+06 | 1.64316e+14 | 3.90701 | 107.015% | 4.19946e+06 | 3.99455e+07 |


### Interpretação do MLP Regressor

Diante dos valores expostos na tabela de métricas, podemos perceber que o ```MLP Regressor``` não obteve nenhum resultado satisfatório. 

Para começar, o R² está com valor negativo ```-0.65```. Isso quer dizer que com o aumento das características o salário do jogador diminui. Esse comportamento está completamente contra o pensamento natural de " Qualidades x Salário" do jogador. Não possui sentido, por exemplo, a redução do salário com o aumento da taxa de pontos, ou vice-versa.

Estendendo a análise para as outras métricas, temos que o MAE está em torno de ```US$821.302,00```, e o MSE corrobora esse transtorno com um valor de 14 dígitos decimais.

Outra anomalia apresentada é o valor do MSLE, este deveria estar em torno de 0 e 1, o valor apresentado foi de ```3.90```. Não possuimos explicação para esse comportamento e sendo assim, não é possível afirmar que todas as predições estão abaixo do valor real.

O MAPE está em 107%, ou seja, a variação do valor do erro está , praticamente, duas vezes acima do valor real.
Em relação ao MedAE, temos um valor de ```US$419.946``` dólares. Realizando uma comparação com o MAE, conseguimos constatar que, sendo o MAE maior do que o MedAE, a distribuição dos valores está deslocada para a direita, para valores mais extremos.

O erro máximo foi de, aproximadamente, ```US$3.994.550,00```, valor equivalente ao salário mais alto. 

O _*Deep Learning*_ é uma técnica mais complexa de ser utilizada. Ela requer um entendimento sólido de seus parâmetros. O que não abrange os conhecimentos adquiridos no início do curso.

## Análise comparativa dos modelos

 Random Forest é uma técnica de Machine Learning enquanto Redes Neurais são exclusivas de Deep Learning.

 As Redes Neurais são organizadas em camadas formadas por nós interconectados que contêm uma função de ativação que calcula a saída da rede. As redes neurais são outro meio de aprendizado de máquina no qual um computador aprende a executar uma tarefa analisando exemplos de treinamento. Como a rede neural é vagamente baseada no cérebro humano, ela consistirá em milhares ou milhões de nós interconectados. Um nó pode ser conectado a vários nós na camada abaixo dele, da qual recebe dados, e vários nós acima dele, que enviam dados. Cada ponto de dados de entrada recebe um peso e é multiplicado e adicionado.

 Random Forest é um conjunto de Árvores de Decisão em que o nó final/folha será a classe majoritária para problemas de classificação ou a média para problemas de regressão.

 Diante da quantidade de atributos, o nosso modelo tem de ser capaz de construir uma relação entre as características dos jogadores com o salário dos mesmos. Nesse sentindo, ambos, redes neurais e florestas aleatórias, têm a capacidade de **modelar relações lineares e não lineares complexas**. Devido à sua construção, as Redes Neurais têm um potencial maior.

 Em relação à robustez do modelo, esse deve ser capaz de reproduzir o seu comportamento com uma nova base de dados, ou seja, o algoritmo usado para estimar o modelo deve ser capaz de encontrar as relações e regularidades e não tentar ajustar os dados da melhor maneira possível. Esse modelo deve ser **robusto** o suficiente para evitar o _overfitting_.
 
 Uma forma de forçar isso é reduzir o conjunto de possíveis modelos que podem ser construídos pelo algoritmo. Na literatura, o termo **“complexidade”** é frequentemente usado neste contexto. Simplificando, podemos descrever isso como as possíveis saídas que um modelo pode gerar em relação às possíveis entradas.

 Em redes neurais, por exemplo, o número de neurônios ocultos e o número de suas camadas influenciam na complexidade dos modelos. Em florestas aleatórias, pode-se ajustar o número de árvores ou o tamanho máximo ou profundidade das árvores individuais, por exemplo. Assim, ambas as abordagens oferecem oportunidades para lidar com problemas de complexidade e _overfitting_. Em comparação, as **redes neurais** possuem maior sensibilidade às entradas, enquanto as **florestas aleatórias** garantem maior robustez com o ajuste do número de árvores.

 Em questão de interpretabilidade, esses modelos apresentam certa dificuldade na visualização do seu funcionamento. Centenas ou milhares de neurônios interagindo de maneira complexa dificulta a sua aplicabilidade onde é necessários saber como o processo está sendo executado. Esse problema se estende para as **florestas aleatórias**. Porém, nesse algoritmo, o entendimento de uma única árvore é mais fácil de ser notado e assim a análise pode ser englobada para a floresta.

 Do ponto de vista econômico, os custos e o tempo necessários para a criação de um modelo desempenham um papel importante. Neste contexto, o treinamento de **redes neurais** é muito demorado e computacionalmente intensivo. Além do próprio processo de aprendizagem, também é necessário um grande trabalho preparatório para colocar os atributos na forma necessária. Para encontrar o melhor modelo, várias variantes devem ser calculadas e testadas. Diferentes hiperparâmetros (o número de camadas ou neurônios por camada ou a taxa de aprendizado) podem ser modificados. Diferentes combinações desses hiperparâmetros são testadas na chamada _grid search_. Para cada combinação, um modelo completo deve ser calculado e avaliado. Quanto mais hiperparâmetros existirem, mais combinações terão que ser testadas. Em combinação com o tempo necessário para treinar um modelo, isso resulta em um gasto considerável de tempo e custo. 
 
 **Random Forests** requerem muito menos preparação. Eles podem lidar com recursos binários, recursos categóricos, bem como recursos numéricos e não há necessidade de normalização de recursos. Elas são rápidas para treinar e otimizar de acordo com seu hiperparâmetro. Assim, o custo computacional e o tempo de treinamento são comparativamente baixos. Além disso, uma **Random Forest** pode ser treinada com uma quantidade relativamente pequena de dados. As **redes neurais** geralmente precisam de mais dados para atingir o mesmo nível de precisão. Por outro lado, as **florestas aleatórias** costumam ter pouco ganho de desempenho quando uma certa quantidade de dados é atingida, enquanto as Redes Neurais geralmente se beneficiam de grandes quantidades de dados e melhoram continuamente a precisão. Nesse quesito, como o a base de dados da NBA é sempre atualizada, o modelo **redes neurais** se torna atrativo devido ao seu desempenho ser proporcional ao tamanho do _dataframe_.

 Com a base de dados que utilizamos e o conhecimento disponível, o modelo **Random Forest** foi o melhor em desempenho. Essa comparação foi realizada em relação às métricas apresentadas no resultado e resumidas na tabela abaixo.

  Modelo |R² | MAE (Erro Absoluto Médio) | MSE (Erro Quadrático Médio) | MSLE(Logaritmo do Erro Quadrático Médio) | MAPE(Percentual do Erro Médio Absoluto) | MedAE (Mediana do Erro Absoluto) | Erro Máximo |
 --- |--- |--- |--- |--- |--- |--- |--- |
 MLP| -0.65| 8.21302e+06 | 1.64316e+14 | 3.90701 | 107,015% | 4.19946e+06 | 3.99455e+07 |
  Random Forest Regressor|0.65| 4.21077e+06 | 3.49325e+13 | 0.988728 | 222,154% | 2.60454e+06 | 1.98524e+07 |



Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


## 8. Conclusão

Desenvolvemos uma análise em uma base de dados de vários jogadores da liga de basquete, para prever seus salários.
Com isso, nós desenvolvemos dois modelos de sistemas inteligentes, o Random Forest Regressor e o MLP Regressor. O primeiro modelo teve uma precisão final de 44% e o segundo modelo teve uma precisão final de 48%.
Os sistemas inteligentes não tiveram uma eficácia tão alta, mas com uma uma melhor seleção de filtros, nós podemos chegar em um resultado mais eficaz.

# REFERÊNCIAS

COSTA, Igor Barbosa da; PIRES, C. E. S.; MARINHO, L. B. Sports analytics: Mudando o jogo. In: Tópicos em Gerenciamento de Dados e Informações 2017. Uberlândia, Brasil: [s.n.], 2017. p. 30–61. ISBN 978-85-7669-400-7
https://jornal.usp.br/atualidades/mercado-de-apostas-esportivas-cresce-mas-envolve-riscos-e-cuidados/

BADENHAUSEN, K. (2019). NBA Team Values 2019: Knicks On Top At $4 Billion. URL: https://www.forbes.com/sites/kurtbadenhausen/2019/02/06/nba-team-values-2019-knicks-on-top-at-4-billion/?sh=6304d77ee667.

SHUGHART, W. (2004). Moneyball: The art of winning an unfair game, by Lewis, M. New York and London: Norton, 2003, xv + 288 pp., USD 24.95 (cloth). Managerial and Decision Economics, 25(8), 550–552. doi:10.1002/mde.1220 

PEDROSA, Rodrigo Trindade. Modelos preditivos esportivos aplicados a dados da NBA. Trabalho de Conclusão de Curso (Graduação em Estatística), 47 f. Universidade Federal Fluminense, Instituto de Matemática e Estatística, Niterói, 2021.

SAMPAIO, António Jaime. ANÁLISE DO JOGO EM BASQUETEBOL: DA PRÉ-HISTÓRIA AO DATA MINING. Lecturas: Educación Física y Deportes, Buenos Aires, ed. 15, 08 1999. Disponível em: https://efdeportes.com/efd15/datam.htm. Acesso em: 16 out. 2022.

RAMOS, Sérgio Antunes; MASSUÇA, Luis Miguel; VOLOSSOVITCH, Anna; FERREIRA, António Paulo; FRAGOSO, Isabel. Morphological and Fitness Attributes of Young Male Portuguese Basketball Players: Normative Values According to Chronological Age and Years From Peak Height Velocity. Frontiers in Sports and Active Living, [s. l.], v. 3, 10 jun. 2021. DOI https://doi.org/10.3389/fspor.2021.629453. Disponível em: https://www.frontiersin.org/articles/10.3389/fspor.2021.629453/full. Acesso em: 16 out. 2022.

BAKER, Joseph; WATTIE, Nick. Innate talent in sport: Separating myth from reality. Current Issues in Sport Science, Austria, v. 3, 3 maio 2018. DOI https://doi.org/10.36950/CISS_2018.006. Disponível em: https://bop.unibe.ch/index.php/ciss/article/view/7557. Acesso em: 16 out. 2022.

TORRES-UNDA, Jon; ZARRAZQUIN, Idoia; GIL, Javier; RUIZ, Fátima; IRAZUSTA, Amaia; KORTAJARENA, Maider; SECO, Jesus; IRAZUSTA, Jon. Anthropometric, physiological and maturational characteristics in selected elite and non-elite male adolescent basketball players. Jornal of Sports Sciences: Issue 2, Biscaia, v. 31, p. 196-203, 9 out. 2012. DOI https://doi.org/10.1080/02640414.2012.725133. Disponível em: https://www.tandfonline.com/doi/full/10.1080/02640414.2012.725133. Acesso em: 16 out. 2022.

LORENZO, Jorge; LORENZO, Alberto; CONTE, Daniele; GIMÉNEZ, Mario. Long-Term Analysis of Elite Basketball Players’ Game-Related Statistics Throughout Their Careers. Frontiers in Pyschology, Kaunas, v. 10, ed. 421, 27 fev. 2019. DOI https://doi.org/10.3389/fpsyg.2019.00421. Disponível em: https://www.frontiersin.org/articles/10.3389/fpsyg.2019.00421/full. Acesso em: 16 out. 2022.


# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).



