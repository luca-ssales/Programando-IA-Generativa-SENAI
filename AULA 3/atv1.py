import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import numpy as np

estudos = pd.DataFrame({
    'notas': [1, 2, 4, 6, 8, 10],
    'horas': [2, 4, 5, 7, 9, 10]
})

X = np.array(estudos['horas'], dtype=float)
y = np.array(estudos['notas'], dtype=float)

print("Dados de entrada (Horas):", X)
print("Dados de saída (Notas):", y)
print("-" * 40)

modelo = Sequential([
    Dense(units=1, input_shape=[1])
])

modelo.compile(
    optimizer='sgd', 
    loss='mean_squared_error'
)

modelo.summary()
print("-" * 40)

print("Treinando o modelo...")
historico = modelo.fit(X, y, epochs=500, verbose=0)
print("Treinamento concluído!")
print("-" * 40)

horas_teste = np.array([6.0], dtype=float)
previsao = modelo.predict(horas_teste)

print(f"Previsão para {horas_teste[0]} horas de estudo:")
print(f"Nota prevista: {previsao[0][0]:.2f}")

