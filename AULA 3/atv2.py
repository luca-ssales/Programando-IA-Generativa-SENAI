import pandas as pd
from sklearn.linear_model import LinearRegression

gamer = pd.DataFrame({
    'horas_jogo': [1, 2, 4, 6, 8, 10],
    'cansaco': [1, 2, 3, 5, 8, 10]
})


X = gamer[['horas_jogo']]

y = gamer['cansaco']

modelo = LinearRegression()

modelo.fit(X, y)

horas = pd.DataFrame({
    'horas_jogo': [7]
})

previsao = modelo.predict(horas)

print(f"Cansaço previsto para 7 horas de jogo: {previsao[0]:.2f}")

print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")