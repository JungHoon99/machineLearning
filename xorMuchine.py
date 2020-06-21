from tensorflow import keras
import numpy as np
import time

x_data=[[0,0],[0,1],[1,0],[1,1]]
y_data=[[0],[1],[1],[0]]

x_data=np.array(x_data)
y_data=np.array(y_data)

model=keras.Sequential()

model.add(keras.layers.Dense(8,activation="sigmoid",input_shape=(2,)))
model.add(keras.layers.Dense(1,activation="sigmoid"))

optimizer=keras.optimizers.SGD(lr=0.1)

model.compile(optimizer=optimizer,loss="binary_crossentropy",metrics=['accuracy'])
model.summary()

model.fit(x_data,y_data,batch_size=3,epochs=2000)

test=[[0,0],[1,1]]
test=np.array(test)

predict=model.predict(x_data)
print(np.round(predict))
time.sleep(5)
