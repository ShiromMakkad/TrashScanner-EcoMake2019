import os
import random

def main():
    subsets = ['train','test']
    waste_types = ['cardboard','glass','metal','paper','plastic','trash']

    training = os.listdir(os.getcwd() + "\\data\\training")

    for i in training:
        trashTypes = os.listdir(os.getcwd() + "\\data\\" + i)
        for j in trashTypes:
            print(j)

    tfms = get_transforms(do_flip=True,flip_vert=True)
    data = ImageDataBunch.from_folder(Path(os.getcwd()),test="test",ds_tfms=tfms,bs=16)

    learn = create_cnn(data,models.resnet34,metrics=error_rate)

if __name__ == "__main__":
    main()