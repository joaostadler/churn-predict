#Inicie importando as bibliotecas necessárias. (Comumente importamos outras além das mencionadas abaixo para análise exploratória, visualizações e outros testes antes da execução.)

import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as pltt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import confusion_matrix

#Leia a sua base de dados que servirá para a criação do modelo preditivo.

df = pd.read_csv(caminho_do_arquivo_csv.csv, decimal=’.’)

#Elimine a coluna onde contém a informação alvo que queremos descobrir posteriormente.

X = dados.drop("churn", axis=1)
y = dados["churn"]

#Separe o conjunto de dados entre dados para treino e dados para testes. Normalmente usamos 20% para testes, podendo ser alterado conforme a sua realidade.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

#Aplique o método que desejar, em nosso exemplo será o Logistic Regression, que é um modelo estatístico usado para estimar a probabilidade de um evento acontecer, SIM ou NÃO.

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

#Uma forma de pré-validar o modelo é utilizar-se do flatten em cima dos dados testados, exemplo:

y_predict = model.predict(X_test)
actual_vs_predict = pd.DataFrame({'Actual': y_test.flatten(),
                                  'Predict': y_predict.flatten()})


# Visualize o resultado e irá perceber sê o valor atual e o valor de predição se está  batendo.
print(actual_vs_predict)


Após isso utilize outros recursos como por exemplo a Matriz de Confusão para novas validações:

A matriz de confusão te dará visibilidade sobre verdadeiros positivos, verdadeiros negativos, falsos negativos e falsos positivos, de forma simples, quantas previsões um modelo acertou e errou ao comparar o que ele previu com o que realmente aconteceu. 

Outra forma adicional de validação é usando o método ROC

# EXEMPLO DE VALIDAÇÃO ROC.
print('O modelo teve uma acurácia de %.2f' % (roc_auc_score(y_test,y_predict)*100), '%')


Esse resultado mostra quais variáveis mais influenciam o churn, sê desejar poderá aplicar diretamente em sua base de dados atual e fazer a predição com dados apenas de clientes ativos, por exemplo. Para isso basta fazer a leitura do dataframe atual com as mesmas variáveis, mesma formatação mas sem a coluna target (pois ela utilizará do modelo).
Para fazer a previsão em cima do novo dataframe realize o seguinte:
#LEITURA DO NOVO DF
dfprevisao = df.read_csv('seu_arquivo.csv', decimal=',')


#APLICANDO A PREDIÇÃO
previsao = model.predict(dfprevisao)
