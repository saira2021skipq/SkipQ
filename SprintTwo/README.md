### SkipQ [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://www.skipq.org/)
# Web Health Monitoring
### SkipQ Cohort 2021: Sprint One 

This project implements a periodic lambda function to check website status. Main focus of the project is to use aws cdk to create cloud infrastructure


### Motivation
Infrastructure as code has quickly become a go-to process to automatically provision and manage cloud resources. With increasing sophistication, engineers and DevOps teams are codifying infrastructure for greater application flexibility and functionality, with a single-source language across an organization.


IT teams have two AWS-native options for infrastructure as code -- AWS CloudFormation and the AWS Cloud Development Kit (CDK). CloudFormation templates were AWS' first foray into cloud-based infrastructure as code, and while still useful, CloudFormation has clear weaknesses. More specifically, it doesn't offer built-in logic capabilities and has a steep learning curve.

The AWS CDK, an open source software development framework to define cloud infrastructure, addresses these weaknesses. The AWS CDK supports popular programming languages, which developers can use to build, automate and manage infrastructure based on an imperative approach. Finally, developers can provision these commands through CloudFormation.

As an extensible, open software development framework, the AWS CDK features integrated development environment (IDE) capabilities. As of publication, the AWS CDK supports TypeScript, JavaScript, Python, Java and C#/.Net. In this article, we'll compare the AWS CDK vs. CloudFormation, including their key features, the role of constructs in building application stacks and the benefits of using a common language for AWS-native infrastructure as code.

## Project Functional Requirements [![Generic badge](https://img.shields.io/badge/Implemented-Yes-<COLOR>.svg)](https://github.com/saira2021skipq/hello_lambda)
* Project must be implemented on Cloud 9
* Project must be implemented in python
* Cloud infrastructure must be created programmatically
* Project must be implemented using Lambda function from awd_cdk
* Lambda function must return status of url passed
* Lambda function must run every 5 minute to monitor website
* Create metrics on cloud watch for each latancy and availability data point for each url
* Set and alram on cloudwatch metrics
* Enable sns email notification service on Alarms

## Project Non Functional Requirements [![Generic badge](https://img.shields.io/badge/Implemented-Yes-<COLOR>.svg)](https://github.com/saira2021skipq/hello_lambda)
* Comments must be add in the code
* Code must be structured well
* Modular approach should be used
* Unnecessary global variables must not be used
* Best practices must be followed 


## Technologies Used
* python [![Generic badge](https://img.shields.io/badge/Python.org--<COLOR>.svg)](https://www.python.org/)
* aws cloud9 
* aws_cdk 
* aws lambda
* aws Cloudwatch
* boto3

## End results
### Cloud watch Metrics   [![Generic badge](https://img.shields.io/badge/image--<COLOR>.svg)](https://github.com/saira2021skipq/SkipQ/tree/master/SprintTwo/images)
![Metrics Result](images/metrics.png?raw=true "Title")
### Alarms  [![Generic badge](https://img.shields.io/badge/image--<COLOR>.svg)](https://github.com/saira2021skipq/SkipQ/tree/master/SprintTwo/images)
![Alarm Result](images/alarm.png?raw=true "Title")
### Email Notification  [![Generic badge](https://img.shields.io/badge/image--<COLOR>.svg)](https://github.com/saira2021skipq/SkipQ/tree/master/SprintTwo/images)
![Email Result](images/email.png?raw=true "Title")

## To run 
#### 1. login to IAM account  [![Generic badge](https://img.shields.io/badge/Login--<COLOR>.svg)](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2)
#### 2. Create a virtual environment in Cloud9
#### 3. Check python version

`python --version`

if it is not python 3

`vim ~/.bashrc`

add this line in the end of bash file

`alias python="/usr/bin/python3"`
#### 4. Choose python language

`cdk init app -language python`

#### 5. Start a virtual environment

`source .venv/bin/activate`

#### 6. Install requirements

`pip install -r requirements.txt`

#### 7. Create Cloud Formation

`cdk synth`
#### 8. Deploy Cloud Formation

`cdk deploy`
