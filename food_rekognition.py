import urllib.request
import boto3


class FoodRekognition:
    @classmethod
    def is_food(cls, image_url):

        s3 = boto3.client('s3')

        bucket = 'ubhackingfoodie'
        file_name = "temp.jpg"

        client = boto3.client('rekognition')
        with urllib.request.urlopen(image_url) as url:
            with open('temp.jpg', 'wb') as f:
                f.write(url.read())

        s3.upload_file(file_name, bucket, file_name)

        detected_labels = client.detect_labels(Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': file_name
            }
        }, MinConfidence=75)
        for label in detected_labels['Labels']:
            # print(label['Name'] + ' : ' + str(label['Confidence']))
            if label['Name'] == "Food" and label['Confidence'] > 80:
                return True
            return False
