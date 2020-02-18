# MTCNN

Updated `pytorch` implementation of **inference stage** of face detection algorithm described in  
[Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks](https://arxiv.org/abs/1604.02878). 
![example of a face detection](images/example.png)


## Requirements
* pytorch >= 1.0
* Pillow >= 6


## How to install
```bash
git clone https://github.com/yl1991/pytorch-mtcnn.git
cd pytorch-mtcnn 
pip install -e .
```

## How to use
```python
from mtcnn import detect_faces
from PIL import Image

image = Image.open('image.jpg')
bounding_boxes, landmarks = detect_faces(image)
```
For examples see `test_on_images.ipynb`.

## Credit
This implementation is heavily inspired by:
* [TropComplique/mtcnn-pytorch](https://github.com/TropComplique/mtcnn-pytorch)
* [pangyupo/mxnet_mtcnn_face_detection](https://github.com/pangyupo/mxnet_mtcnn_face_detection)  
