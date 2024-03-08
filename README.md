# US-Visa-Approval-Prediction

# Git commands
git add .

git commit -m "Updated"

git push origin main

# How to run?

conda create -n venv python=3.8 -y

conda activate venv/

pip install -r requirements.txt

# work flow for data ingestion
1]constant

2] config_entity

3]artifact_entity

4]conponent

5]pipeline

6]app.py / demo.py

# Export environment variable
export MONGODB_URL = "mongodb+srv://remaining string from mongodb to connect to cluster"

export AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"

export AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"


# AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
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