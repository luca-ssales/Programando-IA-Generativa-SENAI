import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

tf.random.set_seed(42)

herois = pd.DataFrame({
    'forca': [1, 2, 3, 7, 8, 10],
    'heroi': [0, 0, 0, 1, 1, 1]
})

X = herois[['forca']]
y = herois['heroi']

modelo = Sequential([
    Dense(1, activation='sigmoid', input_shape=(1,))
])

modelo.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

modelo.fit(X, y, epochs=500, verbose=0)

novo_heroi = np.array([[6]])

probabilidade = modelo.predict(novo_heroi, verbose=0)[0][0]

if probabilidade >= 0.5:
    classificacao = "Herói Forte"
else:
    classificacao = "Herói Fraco"

print(f"Probabilidade: {probabilidade * 100:.2f}%")
print(f"Classificação: {classificacao}")