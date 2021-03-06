# Azure Databricks & Azure Machine Learning MLOps Sample

This is code repository for [Azure Databricks](https://docs.microsoft.com/en-us/azure/databricks/scenarios/what-is-azure-databricks) and [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml) [MLOps](https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment) sample. This sample contain Model Training (using Azure Databricks), Model API (package as container) and Model Web UI (package as container). This sample prediction model is using [classic dataset of diabetes classification](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv). And it's using [Scikit-Learning model framework](https://scikit-learn.org/stable/) to train and export model file in pickle. For Model API, it's using [Flask](https://flask.palletsprojects.com/en/1.1.x/) to interact with pickle model to serve as API. For Model Web UI, it's using Flask to construct simple web user interface for easier interaction with Model API.

**Model API**
* Under folder (Model_API)
* serve.py > Program to start Model API' Flask web server.
* requirments.txt > Required Python packages.
* test.py > Program to test Model API.
* Dockerfile > Docker file to package as container.
* model/ > Pre-trained model files.

**Model Web UI**
* Under folder (Model_Web)
* serve.py > Program to start Model Web UI' Flask web server.
* requirments.txt > Required Python packages.
* Dockerfile > Docker file to package as container.
* templates/ > HTML file.

**Model Training**
* Under folder (Model_Training)
* Model-Training.ipynb > Azure Databricks notebook for Model Training, Model and Experiment Management with Azure Machine Learning.


![diagram1](https://github.com/easonlai/ADB_AML_MLOps_Sample/blob/master/git-images/diagram1.PNG)


