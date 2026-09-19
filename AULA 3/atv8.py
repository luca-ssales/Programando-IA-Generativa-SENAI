import pandas as pd
from sklearn.linear_model import LinearRegression

usica = pd.DataFrame({
    'bpm': [80, 90, 100, 120, 140],
    'viral': [1, 2, 4, 7, 10]
})

X = usica[['bpm']]
y = usica['viral']

modelo = LinearRegression()

modelo.fit(X, y)

nova_musica = pd.DataFrame({
    'bpm': [110]
})

previsao = modelo.predict(nova_musica)

print(f"Nível de viralização previsto para 110 BPM: {previsao[0]:.2f}")
print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")