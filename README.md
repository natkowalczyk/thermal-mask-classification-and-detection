# Thermal mask on face classification and detection
Mask detection and classification in thermal face images




This repository allows to test mask detection and classification models on thermal images.


## Mask detection


## Mask classification
The proposed solution based on semi-supervised CNN with Convolutional Autoencoder (CAE) was provided in the [classification folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/classification). To test the model you can use thermal images of three types of mask given in [images folder](https://github.com/natkowalczyk/thermal-mask-classification-and-detection/tree/main/images).

> Requirements

> For installing the rest of the required packages, run the following command:

> ```
> pip install -r requirements.txt
> ```

To run mask classification you should use:
```bash
>> python mask_classification.py --img_path <path to image>
```

For example:
`python mask_classification.py --img_path ../images/cloth.jpg`

## Paper citation
