# import the boto3 moodule 
import boto3

# open up a session using our role instead of using hard coded keys
dev = boto3.Session(profile_name='luit-user')

# setup our client
sqs = boto3.client('sqs')

# Option 1: Hardcode the queue name directly into your queue creation below 
# Option 2: Request input from user on the name of the queue and covert the response to a string (better option in my opinion)
q_name = str(input("What do you want to name your SQS Queue? "))

# Create our SQS queue and pass our q_name variable into the QueueName
response = sqs.create_queue(
    QueueName=q_name
) 

# Print the response to extract the JSON URL that we are going to require to make the api calls later on
print("SQS Queue Created:", response["QueueUrl"])
