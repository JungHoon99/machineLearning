import tensorflow as tf

x_train = tf.constant([[0, 0], [0, 1], [1, 0], [1, 1]])
x_data = tf.constant([[0], [1], [1], [0]])

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(2, )),
    tf.keras.layers.Dense(4, activation='sigmoid'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'] )

model.fit(x_train, x_data, epochs=2000)