import pandas as pd
from sklearn.linear_model import LogisticRegression

alunos = pd.DataFrame({
    'faltas': [0, 1, 2, 5, 7, 10],
    'resultado': [1, 1, 1, 0, 0, 0]
})

X = alunos[['faltas']]
y = alunos['resultado']

modelo = LogisticRegression()

modelo.fit(X, y)

novo_aluno = pd.DataFrame({
    'faltas': [3]
})

previsao = modelo.predict(novo_aluno)

probabilidade = modelo.predict_proba(novo_aluno)

if previsao[0] == 1:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Resultado para 3 faltas: {resultado}")
print(f"Probabilidade de reprovação: {probabilidade[0][0] * 100:.2f}%")
print(f"Probabilidade de aprovação: {probabilidade[0][1] * 100:.2f}%")