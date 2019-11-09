import os
import random
from fastai.vision import *

def main():
    tfms = get_transforms(do_flip=True,flip_vert=True)
    path = Path(os.getcwd())/"data"
    data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16)

    learn = create_cnn(data,models.resnet34,metrics=error_rate,num_workers=0)
    learn.model
    learn.lr_find(start_lr=1e-6,end_lr=1e1)
    learn.recorder.plot()
    learn.fit_one_cycle(20,max_lr=5.13e-03)
    preds = learn.get_preds(ds_type=DatasetType.Test)
    print(preds[0].shape)
    preds[0]
    data.classes
    max_idxs = np.asarray(np.argmax(preds[0],axis=1))
    yhat = []
    for max_idx in max_idxs:
        yhat.append(data.classes[max_idx])
    yhat
    learn.data.test_ds[0][0]

    y = []

    ## convert POSIX paths to string first
    for label_path in data.test_ds.items:
        y.append(str(label_path))

    ## then extract waste type from file path
    pattern = re.compile("([a-z]+)[0-9]+")
    for i in range(len(y)):
        y[i] = pattern.search(y[i]).group(1)

    print(yhat[0:5])
    ## actual values
    print(y[0:5])
    learn.data.test_ds[0][0]


    cm = confusion_matrix(y,yhat)
    print(cm)
    df_cm = pd.DataFrame(cm,waste_types,waste_types)
    plt.figure(figsize=(10,8))
    correct = 0
    sns.heatmap(df_cm,annot=True,fmt="d",cmap="YlGnBu")

    for r in range(len(cm)):
        for c in range(len(cm)):
            if (r==c):
                correct += cm[r,c]

    accuracy = correct/sum(sum(cm))
    accuracy

if __name__ == "__main__":
    main()