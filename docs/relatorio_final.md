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

Mostre também as **justificativas** para o  desenvolvimento do seu trabalho e, caso deseje, 
destaque alguma contribuição do trabalho.

A justific ativa deve descrever a importância ou a motivação para o desenvolvimento do 
sistema inteligente escolhido. Indique as razões pelas quais você escolheu seus objetivos 
específicos ou as razões para aprofundar em certos aspectos do software.

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)



##    Público alvo

Descreva quem serão as pessoas que usarão a sua aplicação indicando os diferentes perfis. 
O objetivo aqui não é definir quem serão os clientes ou quais serão os papéis dos usuários 
na aplicação. A ideia é, dentro do possível, conhecer um pouco mais sobre o perfil dos 
usuários: conhecimentos prévios, relação com a tecnologia, relações
hierárquicas, etc.

Adicione informações sobre o público-alvo por meio de uma descrição textual, 
diagramas de personas e mapa de stakeholders.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)


## Análise exploratórida dos dados

###    Dicionário de dados

Apresente uma descrição das bases de dados a serem utilizadas. 
Dicionários de dados devem conter as bases de dados, os nomes dos atributos 
com seu significado, seu tipo (inteiro, real, textual, categórico, etc).

Este projeto deve utilizar pelo menos duas fontes de dados. Uma fonte principal e 
uma fonte para enriquecimentos dos dados principais.


###    Descrição de dados

Utilize a análise descritiva baseada em estatística de primeira ordem para descrever os dados.
Como descrever dados numéricos: média, desvio padrão, mínimo, máximo, quartis, histograma, etc.
Como descrever dados qualitativos (categóricos): moda (valor mais frequente), quantidade de valores distintos (categorias), distribuição das categorias (histograma), etc.


## Preparação dos dados

A preparação dos dados consiste dos seguintes passos:

> - Seleção dos atributos
> - Tratamentos dos valores faltantes ou omissos: remoção, substituição, indução, etc.
> - Tratamento dos valores inconsistentes: conversão, remoção de dados duplicados, remoção ou tratamento de ouliers.
> - Conversão de dados: p. ex. numérico para categórico, categórico para binário, etc.


## Indução de modelos

### Modelo 1: Algoritmo


Substitua o título pelo nome do algoritmo que será utilizado. P. ex. árvore de decisão, rede neural, SVM, etc.
Justifique a escolha do modelo.
Apresente o processo utilizado para amostragem de dados (particionamento, cross-validation).
Descreva os parâmetros utilizados. 
Apresente trechos do código utilizado comentados. Se utilizou alguma ferramenta gráfica, apresente imagens
com o fluxo de processamento.

### Modelo 2: Algoritmo

Repita os passos anteriores para o segundo modelo.


## Resultados

### Resultados obtidos com o modelo 1.

Apresente aqui os resultados obtidos com a indução do modelo 1. 
Apresente uma matriz de confusão quando pertinente. Apresente as medidas de performance
apropriadas para o seu problema. 
Por exemplo, no caso de classificação: precisão, revocação, F-measure, acurácia.

### Interpretação do modelo 1

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.


### Resultados obtidos com o modelo 2.

Repita o passo anterior com os resultados do modelo 2.

### Interpretação do modelo 2

Repita o passo anterior com os parâmetros do modelo 2.


## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.

| Modelo | R² | Erro Absoluto Médio | Erro Médio Quadrático | Erro Médio Absoluto Percentual | Erro Máximo |
|--- |--- |--- |--- |--- |--- |
| Random Forest Regressor | 0.7372438637859644| 3513071.36 | 26243521604653.16 | 2% | 19609181.55 |
| MLP Regressor | -0.29405790267121135 | 8136892.21 | 129247739047131.02 | 4% | 36464941.33 |

### Como podemos perceber o ```Random Forest``` apresentou todos os parametros melhores do que ```MLP```. A descrepância se inicia no coeficiente ```R²```, onde o valor negativo do ```MLP``` já o acusa de falta de ajuste. 
### O ```erro médio absoluto```, para os 2 modelos, está bem abaixo do ```maior salário US$43006362.0```, entretanto, para o ```MLP```, o erro tem US$4623820.85 unidade a mais, o que ```representa %131,61``` a mais do que o valor MAE no ```Random Forest```. Desta maneira, esta é outra métrica que pode ser considerada para mostrar a superioridade do Random Forest
### Os valores preditos, nos 2 modelos, apresentaram outliers. Esse comportamento, pode ser confirmado através do ```erro quadrático médio```, quanto maior o valor, maior é a descrepancia da previsão para o real.
### Em relação ao ```MAPE(Erro Médio Absoluto Percentual)``` podemos perceber que no ```Random Forest Regressor``` em média o valor da previsão está 2% defasado.Enquanto no ```MLP``` temos um valor de 4% 
### Desta forma, realizando as comparações, não é dificil supor que o ```erro máximo``` estará no ```MLP```, o que de fato é verdade, e este valor esta ```US$16855759.78``` a mais, representando uma defasagem de ```85%``` em relação ao erro máximo do ```Random Forest```. 
### Concluindo a análise, e sendo objetivo no propósito do trabalho, dificilmente, esses modelos seram aplicados para a determinar o salário do jogador. Os valores são muito altos para se errar. Para se ter ideia, o erro médio do Random Forest está na casa dos ```US$3 milhões```, o que representa ```R$16 milhoes```. No brasil, essa quantia poderia ser convertida em diversos investimentos.

### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


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



Por exemplo:

**[1]** - _ELMASRI, Ramez; NAVATHE, Sham. **Sistemas de banco de dados**. 7. ed. São Paulo: Pearson, c2019. E-book. ISBN 9788543025001._

**[2]** - _COPPIN, Ben. **Inteligência artificial**. Rio de Janeiro, RJ: LTC, c2010. E-book. ISBN 978-85-216-2936-8._

**[3]** - _CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. Rio de Janeiro, RJ: Elsevier, Campus, c2012. xvi, 926 p. ISBN 9788535236996._

**[4]** - _SUTHERLAND, Jeffrey Victor. **Scrum: a arte de fazer o dobro do trabalho na metade do tempo**. 2. ed. rev. São Paulo, SP: Leya, 2016. 236, [4] p. ISBN 9788544104514._

**[5]** - _RUSSELL, Stuart J.; NORVIG, Peter. **Inteligência artificial**. Rio de Janeiro: Elsevier, c2013. xxi, 988 p. ISBN 9788535237016._



# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




