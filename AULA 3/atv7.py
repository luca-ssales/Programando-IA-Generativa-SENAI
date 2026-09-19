import pandas as pd
from sklearn.linear_model import LinearRegression

pizza = pd.DataFrame({
    'tamanho': [20, 25, 30, 35, 40],
    'preco': [20, 30, 40, 50, 60]
})

X = pizza[['tamanho']]
y = pizza['preco']

modelo = LinearRegression()

modelo.fit(X, y)

nova_pizza = pd.DataFrame({
    'tamanho': [32]
})

previsao = modelo.predict(nova_pizza)

print(f"Preço previsto para uma pizza de 32 cm: R$ {previsao[0]:.2f}")
print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")