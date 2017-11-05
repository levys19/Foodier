import boto3
import base64
import requests
from PIL import Image
import urllib.request, io


if __name__ == "__main__":

    # bucket = 'ubhackingfoodie'
    # file_name = "theSOOSH.jpg"
    URL = "https://s3-media4.fl.yelpcdn.com/bphoto/q_XLrURFErX9Kbtd_YSqpQ/o.jpg"
    with urllib.request.urlopen(URL) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())

    img = Image.open('temp.jpg')
    # img_byte = base64.b64encode(img)
    client = boto3.client('rekognition')

    # detected_labels = client.detect_labels(Image={
    #     'S3Object': {
    #         'Bucket': bucket,
    #         'Name': file_name
    #     }
    # }, MinConfidence=75)

    # b = bytearray(response.content)

    detected_labels = client.detect_labels(Image={base64.b64encode(img)}, MinConfidence=75)
    print('Detected labels for Image')
    for label in detected_labels['Labels']:
        if label['Name'] == "Person" and label['Confidence'] > 80:
            print("Not food")
            break
        if label['Name'] == "Food":
            print(label['Name'] + ' : ' + str(label['Confidence']))