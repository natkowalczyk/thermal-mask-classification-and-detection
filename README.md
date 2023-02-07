# Thermal mask on face classification and detection
Mask detection and classification in thermal face images




This repository allows to test mask detection and classification models on thermal images.


## Mask detection
The best model weights are provided in [detection folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/detection) - Yolov5 in "nano" version trained on a thermal images dataset with weights obtained on the COCO set. For this model obtained metrics was:
- precision 0.964 ± 0.025
- recall    0.935 ± 0.006 
- mAP50     0.970 ± 0.013
To run detection you should use [Yolov5 by Ultralytics](https://github.com/ultralytics/yolov5).

## Mask classification
The proposed solution based on semi-supervised CNN with Convolutional Autoencoder (CAE) was provided in the [classification folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/classification). To test the model you can use thermal images of three types of mask given in [images folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/images).

**Requirements**

For installing therequired packages, run the following command:

```
pip install -r requirements.txt
```

**Classify image**

To run mask classification you should use:
```bash
>> python mask_classification.py --img_path <path to image>
```

For example:
`python mask_classification.py --img_path ../images/cloth.jpg`

## Paper citation
