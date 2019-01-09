import boto3
import time
client = boto3.client('sqs')

while True:
    response= client.list_queues()
    
    print('------------------')
    if 'QueueUrls' in response:
        queues=response['QueueUrls']
        for q in queues:
            print(q)
    else:
        print("No Queues Found!!!")
    time.sleep(5)
    print('------------------')
