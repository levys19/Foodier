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
        # for label in detected_labels['Labels']:
        #     print(label['Name'] + ' : ' + str(label['Confidence']))
        for label in detected_labels['Labels']:
            if label['Name'] == "Building" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Logo" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Menu" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Person" and label['Confidence'] > 70:
                return False
            if label['Name'] == "People" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Vehicle" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Rust" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Furniture" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Room" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Pub" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Indoors" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Car" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Appliance" and label['Confidence'] > 70:
                return False
            if label['Name'] == "Food" and label['Confidence'] > 90:
                return True
