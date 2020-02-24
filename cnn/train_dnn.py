import numpy
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils


# Задаем seed для повторяемости результатов
numpy.random.seed(42)

# Загрузка данных для обучения
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Нормализуем данные о интенсивности пикселов изображений
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Преобразуем метки классов в категории
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_tets, 10)

# Создаем модель
model = Sequential()

# Первый сверточный слой
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
