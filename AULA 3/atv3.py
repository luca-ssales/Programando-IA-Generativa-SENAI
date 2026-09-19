import pandas as pd
from sklearn.linear_model import LinearRegression

sorvete = pd.DataFrame({
    'temperatura': [18, 20, 24, 27, 30, 35],
    'vendas': [20, 25, 40, 55, 70, 100]
})

X = sorvete[['temperatura']]
y = sorvete['vendas']

modelo = LinearRegression()

modelo.fit(X, y)

temperatura = pd.DataFrame({
    'temperatura': [28]
})

previsao = modelo.predict(temperatura)

print(f"Vendas previstas para 28°C: {previsao[0]:.2f}")
print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")