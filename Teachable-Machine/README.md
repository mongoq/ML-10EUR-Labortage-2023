# To create the ML model

https://teachablemachine.withgoogle.com/train/image

Take pictures, train, download as TensorFLow Keras model, unzip files keras_model.h5 and labels.txt to folder.

Run to install: 

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

This will use tensorflow-cpu and will not complain about a missing Nvidia GPU.

Enclosed keras_model.h5 and labels.txt will detect the classes - santa, cup and empty.

And finally:

python3 classify1.py
