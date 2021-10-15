# Web Health Monitering
### SkipQ Cohort 2021: Sprint One
This project implements a periodic lambda function to check website status. Main focus of the project is to use aws cdk to create cloud infrastructure


### Motivation
Infrastructure as code has quickly become a go-to process to automatically provision and manage cloud resources. With increasing sophistication, engineers and DevOps teams are codifying infrastructure for greater application flexibility and functionality, with a single-source language across an organization.


IT teams have two AWS-native options for infrastructure as code -- AWS CloudFormation and the AWS Cloud Development Kit (CDK). CloudFormation templates were AWS' first foray into cloud-based infrastructure as code, and while still useful, CloudFormation has clear weaknesses. More specifically, it doesn't offer built-in logic capabilities and has a steep learning curve.

The AWS CDK, an open source software development framework to define cloud infrastructure, addresses these weaknesses. The AWS CDK supports popular programming languages, which developers can use to build, automate and manage infrastructure based on an imperative approach. Finally, developers can provision these commands through CloudFormation.

As an extensible, open software development framework, the AWS CDK features integrated development environment (IDE) capabilities. As of publication, the AWS CDK supports TypeScript, JavaScript, Python, Java and C#/.Net. In this article, we'll compare the AWS CDK vs. CloudFormation, including their key features, the role of constructs in building application stacks and the benefits of using a common language for AWS-native infrastructure as code.

## Project Functional Requirements
* Project must be implemented on Cloud 9
* Project must be implmeneted in python
* Cloud infrastructure must be created programmatically
* Project must by imeplemented using Lambda function from awd_cdk
* Lambda function must return stauts of url passed
* Lambda function must run every 5 minute to moniter website

## Project Non Functional Requirements
* Comments must be add in the code
* Code must be structured well
* Modular approach should be used
* Unnecessory global variables must not be used
* Best practices must be followed 


## Technologies Used
* python 
* aws cloud9
* aws_cdk 
* aws lambda

## End results
### Response
![Response_Result](images/Response.png?raw=true "Title")
### Lambda Monitering 
![Moniter_Result](images/Moniter.png?raw=true "Title")

##To run 
* login to IAM AWS account
* Create an environment in Cloud9
* Check python version
`python --version`
if it is not python 3
`vim ~/.bashrc`
add this line of in the end of bash file
`alias python="/usr/bin/python3"`
create a virtual environment 


