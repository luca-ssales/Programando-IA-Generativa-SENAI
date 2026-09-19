import pandas as pd
from sklearn.linear_model import LinearRegression

pets = pd.DataFrame({
    'passeios': [1, 2, 3, 4, 5],
    'felicidade': [2, 4, 5, 8, 10]
})

X = pets[['passeios']]
y = pets['felicidade']

modelo = LinearRegression()

modelo.fit(X, y)

novo_pet = pd.DataFrame({
    'passeios': [6]
})

previsao = modelo.predict(novo_pet)

print(f"Felicidade prevista para 6 passeios: {previsao[0]:.2f}")
print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")