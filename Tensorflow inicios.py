import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt

celcius = np.array([-40, 10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras.layers.Dense(units=1 ,input_shape=[1])
modelo =tf.keras.Secuential([capa])

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

print(f"comenzando entrenamiento....\n")
historial = modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)
print("¡Modelo entrenado!")

plt.xlabel("#Epoca")
plt.ylabel("Magnitud de Perdida")
plt.plot(historial.history["loss"])

print("Hagamos una prediccion:...")
resultado = modelo.predict([40])
print("Hagamos una prediccion:... El resultado es "+  resultado +" en farenheit")