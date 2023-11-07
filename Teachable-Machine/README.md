# To create the ML model

https://teachablemachine.withgoogle.com/train/image

Take pictures, train, download as TensorFLow Keras model, unzip keras_model.h5 and labels.txt to folder.

Run: 

python3 -m venv ./
source ./bin/activate
pip install -r requirements.txt

This will use tensorflow-cpu and will not complain about a missing Nvidia GPU.
