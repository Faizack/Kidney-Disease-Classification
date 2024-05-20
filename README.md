# Kidney Classification using CNN

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

### STEPS:

Clone the repository

```bash
https://github.com/Faizack/Kidney-Disease-Classification
```
### STEP 01- Install Python 3.8 version

download from https://www.python.org/downloads/

```bash
py -3.8 -venv env
```

```bash
source env/Scripts/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Run your package locally
```bash
python setup.py develop
```
### Optional
#### STEP 04- Run your Training Pipelinr
```bash
python main.py 

```
#### STEP 04- Run your Flask Server API
```bash
python app.py 
```







## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/jOmzWK0CT28?si=HKjQBFoIjv6owhSX)


To make your script robust and able to use environment variables either from a `.env` file or from the system environment, you can combine the approaches. Here’s how you can do that:

1. **Check if environment variables are already set in the system.**
2. **If not, load them from the `.env` file.**
3. **Provide clear feedback if any variables are missing.**


##### Running MLflow UI

To start the MLflow UI, you can run the following command in your terminal:

```bash
mlflow ui
```

This command will start the MLflow UI, which you can access through your web browser, typically at `http://127.0.0.1:5000`.

### DagsHub Integration

[DagsHub](https://dagshub.com/) provides a platform for tracking experiments with MLflow. By setting the appropriate environment variables, as shown above, you can integrate your MLflow tracking with DagsHub.

By following these steps, your script will be more flexible, allowing you to configure environment variables through either a `.env` file or directly in the system environment. This makes your setup more robust and easier to manage in different deployment scenarios.


## About MLflow
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model




# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app


