# Thermal mask on face classification and detection
Mask detection and classification in thermal face images



This repository allows testing mask detection and classification models on thermal images.


## Mask classification
The proposed solution based on semi-supervised CNN with Convolutional Autoencoder (CAE) was provided in the [classification folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/classification). This model achieved **91%** accuracy in face mask classification on thermal images.
To test the model you can use thermal images of three types of masks given in the [images folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/images).

**Requirements**

For installing the required packages, run the following command:

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



## Mask detection
The best model weights are provided in the [detection folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/detection) - Yolov5 in "nano" version trained on a thermal images dataset with weights obtained on the COCO set. For this model obtained metrics were:
- precision 0.964 ± 0.025,
- recall    0.935 ± 0.006,
- mAP50     0.970 ± 0.013.

To detect mask on face you can also use images given in [images folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/images).

To run detection you should use [Yolov5 by Ultralytics](https://github.com/ultralytics/yolov5).
```bash
>> python detect.py --weights <path to weights> --source <path to image>
```

For example:
`python detect.py --weights best.pt --source cloth.jpg`



## Paper citation

N. Kowalczyk, M. Sobotka and J. Rumiński, "Mask Detection and Classification in Thermal Face Images," in IEEE Access, vol. 11, pp. 43349-43359, 2023, doi: 10.1109/ACCESS.2023.3272214
