import pandas as pd
from sklearn.linear_model import LinearRegression

cafe = pd.DataFrame({
    'xicaras': [1, 2, 3, 4, 5],
    'energia': [2, 4, 6, 8, 10]
})

X = cafe[['xicaras']]
y = cafe['energia']

modelo = LinearRegression()

modelo.fit(X, y)

novo_cafe = pd.DataFrame({
    'xicaras': [6]
})

previsao = modelo.predict(novo_cafe)

print(f"Energia prevista para 6 xícaras de café: {previsao[0]:.2f}")
print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")