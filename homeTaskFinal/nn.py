import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras import datasets, layers, models
from keras.utils import np_utils
from keras import regularizers
from keras.layers import Dense, Dropout, BatchNormalization
import matplotlib.pyplot as plt
import numpy as np

# Сформируем обучающую и тестувую выборки
(train_images, train_classes), (test_images, test_classes) = datasets.cifar10.load_data()

print(train_images.shape)
print(train_classes.shape)
print(test_images.shape)
print(test_classes.shape)

# Выведем количество классов
print(np.unique(train_classes))
print(np.unique(test_classes))

# Зададим для каждого класса наименование
class_names = ['Самолет', 'Автомобиль', 'Птица', 'Кошка', 'Олень', 'Собака', 'Лягушка', 'Лошадь', 'Корабль', 'Грузовик']

# Просмотр коллекции изображений
plt.figure(figsize=[32, 32])
for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_classes[i][0]])

plt.show()

# Выполним нормализацию, преобразуем пиксели в числовой тип
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')

train_images = train_images / 255
test_images = test_images / 255

num_classes = 10
train_classes = np_utils.to_categorical(train_classes, num_classes)
test_classes = np_utils.to_categorical(test_classes, num_classes)

# Создаем модель нейросети
model = Sequential()

# Ядро 1. Размер 3*3. На вход подается цветное изображение размером 32*32 пикселей
model.add(keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(keras.layers.MaxPool2D(2, 2)) # для уменьшения выборки

# Ядро 2. Размер 3*3
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
model.add(keras.layers.MaxPool2D(2, 2)) # для уменьшения выборки

# Ядро 3. Размер 3*3
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPool2D(2, 2)) # для уменьшения выборки

model.add(keras.layers.Flatten()) # Добавляем выравнивающий слой

model.add(keras.layers.Dense(32, activation='sigmoid')) # Добавляем замыкающий полносвязный слой

model.add(keras.layers.Dense(num_classes, activation='softmax')) # Добавляем полносвязный слой по количеству классов

model.summary()
keras.utils.plot_model(model, "model.png")
model.compile(optimizer='adam', loss=keras.losses.categorical_crossentropy, metrics=['accuracy'])

# Обучение сети (для отладки поставим 5 эпох, чтобы долго не ждать)
history = model.fit(train_images, train_classes, batch_size=64, epochs=5, validation_data=(test_images, test_classes))

# Выведем результат
plt.figure(figsize=[6,4])
plt.plot(history.history['loss'], 'black', linewidth=2.0)
plt.plot(history.history['val_loss'], 'green', linewidth=2.0)
plt.legend(['Training Loss', 'Validation Loss'], fontsize=14)
plt.xlabel('Epochs', fontsize=10)
plt.ylabel('Loss', fontsize=10)
plt.title('Loss Curves', fontsize=12)

plt.figure(figsize=[6,4])
plt.plot(history.history['accuracy'], 'black', linewidth=2.0)
plt.plot(history.history['val_accuracy'], 'blue', linewidth=2.0)
plt.legend(['Training Accuracy', 'Validation Accuracy'], fontsize=14)
plt.xlabel('Epochs', fontsize=10)
plt.ylabel('Accuracy', fontsize=10)
plt.title('Accuracy Curves', fontsize=12)

pred = model.predict(test_images)
print(pred)

pred_classes = np.argmax(pred, axis=1)
print(pred_classes)

fig, axes = plt.subplots(5, 5, figsize=(15,15))
axes = axes.ravel()

for i in np.arange(0, 25):
    axes[i].imshow(test_images[i])
    axes[i].set_title("Реальн.: %s \n Прогноз.: %s" % (class_names[np.argmax(test_classes[i])], class_names[pred_classes[i]]))
    axes[i].axis('off')
    plt.subplots_adjust(wspace=1)

# Сохраним полученную модель
from keras.models import load_model

model.save('cifar10_project_model.h5')
