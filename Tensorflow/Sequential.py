import keras
import os
import numpy

def main():
    datagen = keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    trainingPath = os.getcwd() + "\\data\\train"
    testingPath = os.getcwd() + "\\data\\test"

    trainingImages = []
    trainingLabels = []

    #Read all images into lists with corresponding labels. Add a debugging breakpoint to see data structure
    trainingFolders = os.listdir(trainingPath)
    for i in range(len(trainingFolders)):
        imagePaths = os.listdir(trainingPath + "\\" + trainingFolders[i])
        for j in range(len(imagePaths)):
            #(i * len(imagePaths)) + j will iterate through every item in trainingImages
            trainingImages.append(keras.preprocessing.image.img_to_array(keras.preprocessing.image.load_img(trainingPath + "\\" + trainingFolders[i] + "\\" + imagePaths[j], color_mode="grayscale", target_size=(48,64))))
            trainingLabels.append(i)

    testingImages = []
    testingLabels = []

    testingFolders = os.listdir(testingPath)
    for i in range(len(testingFolders)):
        imagePaths = os.listdir(testingPath + "\\" + testingFolders[i])
        for j in range(len(imagePaths)):
            testingImages.append(keras.preprocessing.image.img_to_array(keras.preprocessing.image.load_img(testingPath + "\\" + testingFolders[i] + "\\" + imagePaths[j], color_mode="grayscale", target_size=(48,64))))
            testingLabels.append(i)

    print("Data loaded")

    #convert to numpy arrays
    trainingImages = numpy.array(trainingImages)
    testingImages = numpy.array(testingImages)

    trainingImages = trainingImages / 255
    testingImages = testingImages / 255

    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape=[48,64,1]))
    model.add(keras.layers.Dense(1536,activation='relu'))
    model.add(keras.layers.Dense(6,activation='softmax'))
    model.summary()

    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(trainingImages, trainingLabels, epochs=20)

    print("Trained")
    model.save("sequentialModel.h5")


if __name__ == "__main__":
    main()