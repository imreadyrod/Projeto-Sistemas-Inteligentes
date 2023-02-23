# Nome do projeto

A NBA é uma das maiores ligas esportivas do mundo e todos os anos movimenta milhões de dólares em patrocínios e apostas.Pelo senso comum, uma equipe de ponta deve possuir os melhores jogadores, os melhores patrocinadores e uma diretoria qualificada para gerir cada jogo ao sucesso. Porém, a trajetória até o troféu conta com diversas variáveis.

Tendo como fonte a API do “*stats.nba.com*”, nossos sensores disponibilizarão dados de mais de 60.000 jogos contendo todos os aspectos da NBA, considerando os times, jogadores, notícias, drafts, salários, entre outros. Do outro lado, o agente atuador será nosso modelo, que a partir das características fornecidas pelos sensores, filtrará apenas os dados relevantes para a predição do salário do jogador, no ano presente.

## Integrantes

* Caio Felix Reis
* Lucas Rocha Van Huysse
* Pedro Henrique Rodrigues da Silva
* Rodrigo de Oliveira Santos

## Professor

* Hugo Bastos de Paula

## Resumo

* Esse trabalho teve como objetivo a previsão dos salários dos jogadores da liga de basquete ``NBA``. A base de dados foi extraída do _Kaggle_ e se encontra no seguinte link **https://www.kaggle.com/datasets/wyattowalsh/basketball**. Diante da inflação dos preços, foi necessário selecionar uma temporada específica para realizar o tratamento. Os jogadores selecionados jogaram no ano de 2020/2021. A limpeza dos dados e a aplicação dos modelos foi realizada na linguagem ``Pyhton``. Utilizamos o ``Random Forest Regresor`` e o ``MLP Regressor`` para realizar a previsão. As ``florestas aleatórias`` tiveram maior desempenho, porém não tão satisfatório. Esse comportamento pode ser relacionado à composição dos dados, como, o tamanho da base, a seleção das variáveis - muitas delas não possuiam uma relação direta com o ``target`` - a seleção correta dos hiperparâmetros do algoritmo. Esse entendimento pode ser estendido para as ``redes neurais``, nesse caso, a baixa performance está completamente atrelada à falta de dados e a manipulação dos seus hiperparâmetros, como taxa de aprendizado, seleção de neurônios e quantidade de camádas. Por fim, o trabalho foi válido para o desenvolvimento das habilidades atreladas à construção de sistemas inteligentes, nele tivemos um prelúdio da coleta de dados, o preparo, a aplicação de um algoritmo e sua avaliçaõ por meios das métricas.

## Itens do Template

* Planilhas utilizadas:
``https://github.com/ICEI-PUC-Minas-PPL-CD/ppl-cd-pcd-sist-int-2022-2-compartilhamento-de-bicicletas/tree/main/src/data``

* Início da manipulação da base de dados:
``https://github.com/ICEI-PUC-Minas-PPL-CD/ppl-cd-pcd-sist-int-2022-2-compartilhamento-de-bicicletas/blob/867f5f6845d07559a283748da371a25b78e6f32f/src/python/main.ipynb``

* Pré processamento:
``https://github.com/ICEI-PUC-Minas-PPL-CD/ppl-cd-pcd-sist-int-2022-2-compartilhamento-de-bicicletas/blob/867f5f6845d07559a283748da371a25b78e6f32f/src/python/preprocess.py``

* Random Forest Regresor:
``https://github.com/ICEI-PUC-Minas-PPL-CD/ppl-cd-pcd-sist-int-2022-2-compartilhamento-de-bicicletas/blob/867f5f6845d07559a283748da371a25b78e6f32f/src/python/model.py``

* MLP Regressor:
``https://github.com/ICEI-PUC-Minas-PPL-CD/ppl-cd-pcd-sist-int-2022-2-compartilhamento-de-bicicletas/blob/867f5f6845d07559a283748da371a25b78e6f32f/src/python/MLPRegressor.py``

*Relatório Final:
``https://github.com/ICEI-PUC-Minas-PPL-CD/ppl-cd-pcd-sist-int-2022-2-compartilhamento-de-bicicletas/blob/867f5f6845d07559a283748da371a25b78e6f32f/docs/relatorio_final.md``


