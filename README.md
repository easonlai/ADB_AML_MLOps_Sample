# Azure Databricks & Azure Machine Learning MLOps Example

This is code repository for Azure Databricks and Azure Machine Learning MLOps example. This sample contain Model Training (using Azure Databricks), Model API (package as container) and Model Web UI (package as container). This sample prediction model is using classic dataset of diabetes classification. And it's using Scikit-Learning model framework to train and export model file in pickle. For Model API, it's using Flask to interact with pickle model to serve as API. For Model Web UI, it's using Flask to construct simple web user interface for easier interaction with Model API.

Model API
* Under folder (Model_API)
* serve.py > Program to start Model API' Flask web server.
* requirments.txt > Required Python packages.
* test.py > Program to test Model API.
* Dockerfile > Docker file to package as container.
* model/ > Pre-trained model files.

Model Web UI
* Under folder (Model_Web)
* serve.py > Program to start Model Web UI' Flask web server.
* requirments.txt > Required Python packages.
* Dockerfile > Docker file to package as container.
* templates/ > HTML file.

Model Training
* Under folder (Model_Training)
