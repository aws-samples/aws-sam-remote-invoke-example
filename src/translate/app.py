# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import boto3
from aws_lambda_powertools import Logger
translate = boto3.client('translate')
logger = Logger()

def lambda_handler(event, context):
    if not 'message' in event:
        logger.error({
            "status": "failure",
            "message": "message not found in event"
        })
        return 'message not found in event'
    
    if not 'target-language' in event:
        logger.error({
            "status": "failure",
            "message": "Target language not found in event"
        })
        return 'Target language not found in event'

    try:
        translated_text = translate.translate_text(
            Text=event['message'],
            SourceLanguageCode='en',
            TargetLanguageCode=event['target-language']
        )
        logger.info({
            "status": "success",
            "logging-message": "The text was successfuly translated"
        })
        return {'translated-message': translated_text['TranslatedText']}
    except Exception as e:
        logger.error({
            "status": "failure",
            "message": e
        })
        return 'There was an error translating the message'