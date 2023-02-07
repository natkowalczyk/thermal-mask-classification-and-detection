from matplotlib import pyplot as plt
import numpy as np
import os
from PIL import Image
from keras.models import load_model
import argparse

parser = argparse.ArgumentParser(description='file_name')

parser.add_argument('--img_path', default="../images/ffp2.jpg", type=str, help='Path to image')
args = parser.parse_args()


path_to_img = args.img_path

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ["SM_FRAMEWORK"] = "tf.keras"

# load model from file
model2 = load_model('autoencoder_classification')


# open img
image = Image.open(path_to_img)
image = image.resize((128, 128))

# prepare image to model
data_img = np.asarray(image)
data_img = data_img[:, :, 0]
data_img = data_img[..., np.newaxis]
data_img = data_img[np.newaxis, ...]

# normalization
data_img = data_img / np.max(data_img)

# predict class for specified image
predicted_class = model2.predict(data_img)

# map predicted class
predicted_classes = np.argmax(np.round(predicted_class),axis=1)

label_dict = {
 0: 'cloth',
 1: 'ffp2',
 2: 'surgery',
}

predicted_class_name = label_dict[predicted_classes[0]]

# print predicted clas
print("Predicted class: " + predicted_class_name)

# show image with predicted class
plt.figure()
plt.imshow(data_img[0, :, :, :], cmap='gray', interpolation='none')
plt.title("Predicted {}".format(predicted_class_name))
plt.show()



