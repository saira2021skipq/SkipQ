
# CI/CD Pipeline using aws cdk

Table of Contents
=================
   * [Table of Contents](#table-of-contents)
   * [Features](#Features)
   * [Project Structure (default aws cdk Tempelate)](#Project-Structure-default-aws-cdk-Tempelate))
   * [Note on CI/CD on aws](#Note-on-CI/CD-on-aws)
   * [Quickstart](#quickstart)
   * [Local steps](#local-steps)
      * [Creating a token](#Creating-a-token)
      * [Add Github credentials to AWS Secrets Manager](#Add-Github-credentials-to-AWS-Secrets-Manager)
      * [AWS Roles](#AWS-Roles)
      * [Importnat changes to code](#Importnat-changes-to-code)
   * [Deployment](#Deployment)
      * [Activate Virtual Environment](#Activate-Virtual-Environment)
      * [Install requirements](#Install-requirements)
      * [Bootstrap the environment with qualifer and toolkit name](#Bootstrap-the-environment-with-qualifer-and-toolkit-name)
      * [Make your first deployment](#Make-your-first-deployment)
   * [Feedback](#feedback)
   * [Contributing](#contributing)
   * [Kudos](#kudos)
## Features

## Project Structure (default aws cdk Tempelate)
```
.
├── lambda_b
│   └── __init__.py
|   └── alarm_defination.py
|   └── cloudWatch_defination.py
|   └── constants.py
|   └── dynamo_db.py
|   └── handler.py
|   └── lambda_database.py
|   └── web_health_publisher.py
├── sprint4
│   └── ProductionStage.py
|   └── __init__.py
|   └── beta_stage.py
|   └── hello_lambda_stack.py
|   └── sprint4_stack.py
├── .gitignore
├── README.md
├── unittests
│   ├── __init__.py
│   └── test_lambda_stack.py
├── setup.py
├── cdk.json
├── requirements.txt
├── source.bat
```

Some explanations regarding structure:
- `lambda_b` folder is a resource folder where constants and functions are implemented.
- `sprint4`  folder contains stacks and stages for pipeline.
- `unittests` - is a package with tests.
- `cdk.json` - deployment configuration file.



## Note on CI/CD on aws

> **_NOTE:_**  
[CI/CD on aws](https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/cicd-on-aws.html) can be pictured as a pipeline, where new code is submitted on one end, tested over a series of stages (source, build, test, staging, and production), and then published as production-ready code.


## Quickstart

> **_NOTE:_**  
As a prerequisite, you need to install [python](https://www.python.org) on cloud9 ([Login](https://us-east-2.console.aws.amazon.com/cloud9/home?region=us-east-2)).
In these instructions we're based on aws services 
If you don't need to use cloud9, we still recommend to use cloud9 because it has linux setup created.

## Local steps
### Creating a token

* [Verify your email address](https://docs.github.com/en/get-started/signing-up-for-github/verifying-your-email-address), if it hasn't been verified yet.

* In the upper-right corner of any page, click your profile photo, then click Settings.
  ![userbar-account-settings.png](images/userbar-account-settings.png?raw=true "Title")
  
* In the left sidebar, click Developer settings.

  ![developer-settings.png](images/developer-settings.png?raw=true "Title")
  
* In the left sidebar, click Personal access tokens.

  ![developer-settings.png](images/personal_access_tokens_tab.png?raw=true "Title")
  
* Click Generate new token.

  ![developer-settings.png](images/generate_new_token.png?raw=true "Title")
* Give your token a descriptive name.

  ![developer-settings.png](images/token_description.png?raw=true "Title")
  
* To give your token an expiration, select the Expiration drop-down menu, then click a default or use the calendar picker

   ![developer-settings.png](images/token_expiration.png?raw=true "Title")
   
* Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select repo.

   ![developer-settings.png](images/token_scopes.gif?raw=true "Title")
   
* Click Generate token.

   ![developer-settings.png](images/generate_token.png?raw=true "Title")
  
### Add Github credentials to AWS Secrets Manager
You will now see your new token so please copy and paste that token to a notepad or anywhere that you can reference it for the next step.

We will be using AWS Secrets Manager to store our GitHub access token so that our CodeBuild project will be able to reference our credentials and have the ability to use our GitHub repository as its source.

```
aws secretsmanager create-secret --name github-oauth-token
          --description "Secret for GitHub" --secret-string "insert your GitHub OAuth token"
          
```

You should see a similar output if the command was able to successfully run.
```
{
    "ARN": "arn:aws:secretsmanager:us-west-2:123456789012㊙️tutorials/MyFirstSecret-rzM8Ja",
    "Name": "github-oauth-token",
    "VersionId": "35e07aa2-684d-42fd-b076-3b3f6a19c6dc"
}
```
If you browse to the AWS Secrets Manager console, you should see two secrets now:

* Secret that holds our credentials for Docker Hub
* Secret that holds our credentials for Github

![developer-settings.png](images/secrets-manager.png?raw=true "Title")
Perform the following actions in your development environment:

### AWS Roles
Make sure you have access to following aws roles
* AWSLambda_FullAccess
* CloudWatchFullAccess
* AmazonDynamoDBFullAccess
* AmazonSNSFullAccess

### Importnat changes in code
* - `/sprint4/sprint4_stack` replace this feild according to your github key stored in aws secret manager
```
output=source_artifact,
        oauth_token=core.SecretValue.secrets_manager('saira_pipeline_token', json_field='saira_pipeline_token'),
        owner='saira2021skipq', 
```
## Deployment

### Activate Virtual Environment
```
Source .venv/bin/activate
```
### Install requirements
```
pip install -r requirements.txt
```
### Bootstrap the environment with qualifer and toolkit name
```
$ cdk bootstrap --qualifier <QualifierName> --toolkit-stack-name <ToolKitName>
```
### Make your first deployment
```
cdk deploy
```

## Feedback
Issues with template? Found a bug? Have a great idea for an addition? Feel free to file an issue.

## Contributing
Have a great idea that you want to add? Fork the repo and submit a PR!

## Kudos
- Project based on the [cookiecutter datascience project](https://drivendata.github.io/cookiecutter-data-science)
- README.md ToC generated via [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)
