import pandas as pd
from sklearn.linear_model import LinearRegression

filmes = pd.DataFrame({
    'duracao': [80, 90, 100, 110, 120],
    'nota': [4, 5, 7, 8, 9]
})

X = filmes[['duracao']]
y = filmes['nota']

modelo = LinearRegression()

modelo.fit(X, y)

novo_filme = pd.DataFrame({
    'duracao': [105]
})

previsao = modelo.predict(novo_filme)

print(f"Nota prevista para um filme de 105 minutos: {previsao[0]:.2f}")
print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")