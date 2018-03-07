import boto3
import os

sns_connect = boto3.client('sns')
phone_number = os.environ.get('ph_number')
sms_subject = os.environ.get('sms_subject')

def send_message(message):
    sns_connect.set_sms_attributes(
        attributes={
            'DefaultSMSType': 'Transactional',
            'DefaultSenderID': str(sms_subject)
        }
    )

    response = sns_connect.publish(
        PhoneNumber=phone_number,
        Message=message
    )
