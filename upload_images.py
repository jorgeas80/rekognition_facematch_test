import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images = [
    ('data/image01.jpeg', 'gala'),
    ('data/image02.jpeg', 'gala'),
    ('data/image03.jpeg', 'gala'),
    ('data/image04.jpeg', 'jorge'),
    ('data/image05.jpeg', 'jorge'),
    ('data/image06.jpeg', 'jorge')
]

# Iterate through list to upload objects to S3
for image in images:
    file = open(image[0], 'rb')
    object = s3.Object('facematch', 'index/' + image[0])
    ret = object.put(Body=file, Metadata={'FullName': image[1]})
