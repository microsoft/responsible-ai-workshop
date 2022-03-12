#Use the azureml provided sklearn image as base. Prebuilt images are still in preview.

FROM mcr.microsoft.com/azureml/sklearn-0.24.1-ubuntu18.04-py37-cpu-inference:20210906.v1

#Install requirements before adding the code, so that the dependencies layer is not rebuilt when the code changes. 

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#Add the python score inference script

COPY score.py /var/azureml-app
ENV AZUREML_ENTRY_SCRIPT=score.py

# Add the model to the image

ENV MODEL_PATH=/var/azureml-app/azureml-models/model.pkl
COPY model.pkl ${MODEL_PATH}
