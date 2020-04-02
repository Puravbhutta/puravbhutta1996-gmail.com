import tensorflow
from tensorflow import keras
from tensorflow.keras.datasets import mnist
import numpy as np
import PIL
import skimage
from skimage import io
from skimage import color



x_train = color.rgb2gray(io.imread(r"C:\Users\Admin\Desktop\AI_project\bmps\1.bmp"))
y_train = [10,15,200,300]


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.constraints import max_norm as maxnorm
from tensorflow.keras.optimizers import SGD

# Create the model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(480, 320, 1), padding='same', activation='relu', kernel_constraint=maxnorm(3)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(62, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(Conv2D(62, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(Conv2D(62, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(Conv2D(16, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dense(100, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dense(4, activation='relu'))

# Compile model
epochs = 1
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='sparse_categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
print(model.summary())

# Fit the model
model.fit(x_train, y_train)

# saving the trained model for predictions
model.save('my_model1.h5')
