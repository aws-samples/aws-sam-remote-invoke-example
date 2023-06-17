# AWS SAM 'remote invoke' test application

This repository contains the demo application for the AWS SAM CLI `remote invoke` command. For a full explanation of 
this application refer to the [blog post](https://aws.amazon.com/blogs/compute/testing-aws-lambda-functions-with-aws-sam-remote-invoke).

## Deploying the application

1. Clone the repository
```
git clone https://github.com/aws-samples/aws-sam-remote-invoke-example.git
```
2. Change to the root directory of the repository
```
cd aws-sam-invoke-example
```
3. Build the application
```
sam build --use-container
```
4. Deploy the application
```
sam deploy --guided
```
Name the project **remote-test** and keep all other defaults

## Cleaning up

Run the following command:
```
sam delete --stack-name remote-test
```