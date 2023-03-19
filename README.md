# Label-data-for-YOLO
Label images with "LabelMe" and transform JSON format into the yolo format (.txt)

This repository aims to prepare the dataset for training a model in YOLOv3 v4 algorithm.
We recommend using other repositories for training the model and labeling the data, respectively  https://github.com/AlexeyAB/darknet.git and https://github.com/LabelMe.

When you have a considerable number of images (a few thousand) you can use the order JPG images python code to order your data. Then we can start labeling the images with LabelMe and get them into the JSON format. We will require the data labeled in XML format, to get this work done you can use the labelme_to_xml python code to transform the form of data to XML.
At this point, the data has two folders one for the images and another for the XML files. 
Next, we need to prepare the data into the darknet file for training the model.

A.	Dataset Preparation:
1.	Create a new folder named "VOCdevkit" inside the darknet folder.
2.	Create a subfolder named "VOC2007" inside the VOCdevkit folder.
3.	Create three subfolders inside the VOC2007 folder and name them as Annotation, ImageSets, and JPEGImages.
4.	Create three files inside the ImageSets folder and name them Layout, Main, and Segmentation.
5.	Place all the images from the dataset in the JPEGImages folder.
6.	Copy all the XML files into the Annotations folder.
7.	Copy the Python program test.py or test.py into the directory containing the ImageSets folder (not inside the ImageSets folder).
Next, in the ImageSets directory we run: python test.py, this will create four new files at Imagesets/Main folder, test, train, trainval and val files.

B.	Then, modify the next direction darknet/cfg/coco.data
classes= 1 # 自己的类别
train  = 2007_train.txt # 由voc_label.py生成
valid  = 2007_test.txt # 由voc_label.py生成
#valid = data/coco_val_5k.list
names = data/coco.names
backup = ./backup #模型的存放位置
eval=coco

C.	Then, move the voc_label.py file into darknet file and make some modifications to sets and classes, according to the necessities.
#we use these three sets
sets =[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#write the name of the classes you want the model to recognize 
classes = ["fire"]

At darknet terminal run: python voc_label.py to transform the label files into .txt form. This will create three files at darknet file and the label data into .txt form at VOC2007/labels file

D.	Next, modify the coco.names files at ./data/coco.names. Check the train and valid directory file. 
classes= 1
train  = /home/liyufeng/test/darknet/2007_train.txt
valid  = /home/liyufeng/test/darknet/2007_test.txt
names = data/coco.names
backup = ./backup/

E.	To train the model we need to download trained weights, yolov4.conv.137 and copied to the darknet file.
F.	Finally, edit the yolov4-custom.cfg file at darknet/cfg/yolov4-custom.cfg
Filters = (number of classes+5)*3
Classes= number of your classes

At this time we can start training the model: 
./darknet detector train cfg/coco.data cfg/yolov4-custom.cfg yolov4.conv.137
