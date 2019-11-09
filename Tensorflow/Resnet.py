import keras
import os
import numpy
import math

def main():
    datagen = keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    trainingPath = os.getcwd() + "\\data\\train"

    trainingImages = []
    trainingLabels = []

    new_width, new_height = 324, 324
    w, h = 512, 324

    #Read all images into lists with corresponding labels. Add a debugging breakpoint to see data structure
    trainingFolders = os.listdir(trainingPath)
    for i in range(len(trainingFolders)):
        imagePaths = os.listdir(trainingPath + "\\" + trainingFolders[i])
        for j in range(len(imagePaths)):
            image = ((keras.preprocessing.image.load_img(trainingPath + "\\" + trainingFolders[i] + "\\" + imagePaths[j], color_mode="rgb")).crop(((w-new_width)//2, (h-new_height)//2, (w+new_width)//2, (h+new_height)//2))).resize((224,224))
            trainingImages.append(keras.applications.resnet50.preprocess_input(keras.preprocessing.image.img_to_array(image)))
            trainingLabels.append(i)

    print("Data loaded")

    #convert to numpy arrays
    trainingImages = numpy.array(trainingImages)
    trainingLabels = numpy.array(trainingLabels)

    #trainingImages = trainingImages / 255

    base_model = keras.applications.resnet50.ResNet50(weights="imagenet", include_top=False, input_shape= (224,224,3), pooling="avg")
    x = base_model.output
    outputLayer = keras.layers.Dense(6, activation= 'softmax')(x)
    model = keras.models.Model(inputs = base_model.input, outputs = outputLayer)

    for layer in model.layers[:-3]:
        layer.trainable = False

    model.summary()

    batchSize = 64
    model.compile(optimizer="adam", loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit_generator(datagen.flow(trainingImages, trainingLabels, batch_size=batchSize),
                        steps_per_epoch=len(trainingImages) // batchSize, epochs=50)

    print("Trained")
    model.save("resnetModel.h5")


if __name__ == "__main__":
    main()
