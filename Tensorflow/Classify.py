import keras
import os
import numpy


def main():
    testingPath = os.getcwd() + "\\data\\test"

    testingImages = []
    testingLabels = []

    new_width, new_height = 324, 324
    w, h = 512, 324

    testingFolders = os.listdir(testingPath)
    for i in range(len(testingFolders)):
        imagePaths = os.listdir(testingPath + "\\" + testingFolders[i])
        for j in range(len(imagePaths)):
            image = ((keras.preprocessing.image.load_img(testingPath + "\\" + testingFolders[i] + "\\" + imagePaths[j],
                                                         color_mode="rgb")).crop(
                ((w - new_width) // 2, (h - new_height) // 2, (w + new_width) // 2, (h + new_height) // 2))).resize(
                (224, 224))
            testingImages.append(keras.applications.resnet50.preprocess_input(keras.preprocessing.image.img_to_array(image)))
            testingLabels.append(i)

    test_datagen = keras.preprocessing.image.ImageDataGenerator()

    print("Data loaded")

    # convert to numpy arrays
    testingImages = numpy.array(testingImages)
    # testingImages = testingImages / 255

    model = keras.models.load_model("resnetModel.h5")
    model.summary()

    batchSize = 64
    predictions = model.predict(testingImages)
    #predictions = model.predict_generator(test_datagen.flow(testingImages, testingLabels, batch_size=batchSize),steps =len(testingImages) // batchSize)

    total = 0
    correct = 0

    unsure = 0
    unsureCorrect = 0

    for i in range(len(predictions)):
        total += 1
        if testingLabels[i] == numpy.argmax(predictions[i]):
            correct += 1


    print("Accuracy: " + str((correct / total) * 100) + "%")


if __name__ == "__main__":
    main()
