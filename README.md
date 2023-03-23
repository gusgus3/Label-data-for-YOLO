# Preparing-data-for-YOLO

## A guide for preparing Dataset to train a model with YOLOv3 v4 algorithm under ROS Melodic and Ubuntu 18.04. 

The present repository aims to guide you during the proces of preparing the Dataset, from labeling images to adding them into YOLO algorithm to train a model with your own data. Every part of this repository is sample code which shows how to do the following:

* Order your data with the order JPG images code
* Label the images with LabelMe open source sofware
* Transform JSON format files to XML format with labelme_to_xml code
* Prepare the Dataset with test and voc_label code

## How to use this repository 

Once you prepare the environment for training a model with YOLOv4 on the darknet 
- [YOLOv4](https://medium.com/@alexeyab84/yolov4-the-most-accurate-real-time-neural-network-on-ms-coco-dataset-73adfd3602fe?source=friends_link&sk=6039748846bbcf1d960c3061542591d7)
then you can start preparing the data with this repository.

About Darknet framework: http://pjreddie.com/darknet/

[![Darknet Continuous Integration](https://github.com/AlexeyAB/darknet/workflows/Darknet%20Continuous%20Integration/badge.svg)](https://github.com/AlexeyAB/darknet/actions?query=workflow%3A%22Darknet+Continuous+Integration%22)
[![CircleCI](https://circleci.com/gh/AlexeyAB/darknet.svg?style=svg)](https://circleci.com/gh/AlexeyAB/darknet)
[![Contributors](https://img.shields.io/github/contributors/AlexeyAB/Darknet.svg)](https://github.com/AlexeyAB/darknet/graphs/contributors)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](https://github.com/AlexeyAB/darknet/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/75388965.svg)](https://zenodo.org/badge/latestdoi/75388965)
[![arxiv.org](http://img.shields.io/badge/cs.CV-arXiv%3A2004.10934-B31B1B.svg)](https://arxiv.org/abs/2004.10934)
[![arxiv.org](http://img.shields.io/badge/cs.CV-arXiv%3A2011.08036-B31B1B.svg)](https://arxiv.org/abs/2011.08036)
[![colab](https://user-images.githubusercontent.com/4096485/86174089-b2709f80-bb29-11ea-9faf-3d8dc668a1a5.png)](https://colab.research.google.com/drive/12QusaaRj_lUwCGDvQNfICpa7kA7_a2dE)
[![colab](https://user-images.githubusercontent.com/4096485/86174097-b56b9000-bb29-11ea-9240-c17f6bacfc34.png)](https://colab.research.google.com/drive/1_GdoqCJWXsChrOiY8sZMr_zbr_fH-0Fg)

First, be sure to get at least a few thousand images for each class you want your model to detect. A good tool is LabelMe. 
- [LabelMe](https://github.com/LabelMe)

LabelMe will give you JSON format labeled files. However, we require the data labeled in XML format, to get this work done you can use the labelme_to_xml python code to transform the form of data to XML.

At this point, the data has two folders one for the images and another for the XML files. 
Next, we need to prepare the data into the darknet file for training the model.

* A.	Dataset Preparation:
    1.	Create a new folder named **"VOCdevkit"** inside the darknet folder.
    2.	Create a subfolder named **"VOC2007"** inside the VOCdevkit folder.
    3.	Create three subfolders inside the **VOC2007**    folder and name them as *Annotation*, *ImageSets*, and *JPEGImages*.
    4.	Create three files inside the **ImageSets** folder and name them *Layout*, *Main*, and *Segmentation*.
    5.	Place all the *images* from the dataset in the **JPEGImages** folder.
    6.	Copy all the *XML files* into the **Annotations** folder.
    7.	Copy the Python program **test.py** into the directory containing the **ImageSets** folder (not inside the ImageSets folder).
Next, in the **ImageSets** directory we run: **python test.py**, this will create four new files at **Imagesets/Main folder**, *test*, *train*, *trainval* and *val* files.

* B.	Then, modify the next direction **darknet/cfg/coco.data**
```ini
classes= 1 # 自己的类别
train  = 2007_train.txt # 由voc_label.py生成
valid  = 2007_test.txt # 由voc_label.py生成
#valid = data/coco_val_5k.list
names = data/coco.names
backup = ./backup #模型的存放位置
eval=coco
```

* C.	Then, move the **voc_label.py** file into **darknet** file and make some modifications to **sets** and **classes**, according to the necessities.
```ini
#we use these three sets
sets =[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#write the name of the classes you want the model to recognize 
classes = ["fire"]
```

At darknet terminal run: python **voc_label.py** to transform the label files into .txt form. This will create three files at darknet file and the label data into .txt form at **VOC2007/labels** file

* D.	Next, modify the coco.names files at **./data/coco.names** Check the train and valid directory file. 
```ini
classes= 1
train  = /home/liyufeng/test/darknet/2007_train.txt
valid  = /home/liyufeng/test/darknet/2007_test.txt
names = data/coco.names
backup = ./backup/
```

* E.	To train the model we need to download trained weights, **yolov4.conv.137** and copied to the darknet file.

* F.	Finally, edit the yolov4-custom.cfg file at **darknet/cfg/yolov4-custom.cfg**
```ini
Filters = (number of classes+5)*3
Classes= number of your classes
```

At this time we can start training the model: 

**`./darknet detector train cfg/coco.data cfg/yolov4-custom.cfg yolov4.conv.137`**
