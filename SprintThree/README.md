### SkipQ [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://www.skipq.org/)
# Web Health Monitoring
### SkipQ Cohort 2021: Sprint One 

This project implements a lambda function to write data to dynamo db received from sns topic

## Project Features 
* A lambda function has been implemented to check website status every 5 minutes
* Website status value are written to cloud watch metric
* Alarms has been set on cloudwatch metrices 
* Everytime alarm changes its state a notifcation is sent to lambda function
* lambda function store alarm message in dynamodb


## Technologies Used
* python [![Generic badge](https://img.shields.io/badge/Python.org--<COLOR>.svg)](https://www.python.org/)
* aws cloud9 
* aws_cdk 
* aws lambda
* aws Cloudwatch
* boto3
* dynamodb
* 
## To run 
#### 1. login to IAM account  [![Generic badge](https://img.shields.io/badge/Login--<COLOR>.svg)](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2)
#### 2. Create a virtual environment in Cloud9
#### 3. Check python version

`python --version`

if it is not python 3

`vim ~/.bashrc`

add this line of in the end of bash file

`alias python="/usr/bin/python3"`

#### 4. Start a virtual environment

`source .venv/bin/activate`

#### 4. Install requirements

`pip install -r requirements.txt`

#### 4. Create Cloud Formation

`cdk synth`
#### 4. Deploy Cloud Formation

`cdk deploy`
