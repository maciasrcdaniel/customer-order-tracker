import boto3
import time


def lambda_handler(event, context):

    # Create SQS client
    sqs = boto3.client('sqs')
    
    # Queue URL from previously created queue
    q_url = 'https://sqs.us-east-1.amazonaws.com/119121491463/customer_order_track'
    
    # Print the current date and time to test
    current_time_date = time.ctime()
    
    # Send message to SQS queue
    response = sqs.send_message(
        # Set the variable QueueUrl to SQS URL
        QueueUrl=q_url,
        # Set the current date and time 
        MessageBody=current_time_date,
    )
    
    print("Message Sent:", response)
    
    return {
        'statusCode': 200,
        'body': "Congrats your message was sent"
    }