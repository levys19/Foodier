import urllib.request
import boto3
from PIL import Image

if __name__ == "__main__":

    s3 = boto3.client('s3')

    bucket = 'ubhackingfoodie'
    file_name = "temp.jpg"

    client = boto3.client('rekognition')
    URL = "https://s3-media4.fl.yelpcdn.com/bphoto/q_XLrURFErX9Kbtd_YSqpQ/o.jpg"
    with urllib.request.urlopen(URL) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())

    img = Image.open('temp.jpg')
    s3.upload_file(file_name, bucket, file_name)

    # img_byte = base64.b64encode(img)

    # detected_labels = client.detect_labels(Image={
    #     'S3Object': {
    #         'Bucket': bucket,
    #         'Name': file_name
    #     }
    # }, MinConfidence=75)

    # print('Detected labels for Image')
    # detected_labels = client.detect_labels(Image={'Bytes': f.read()}, MinConfidence=75)
    # for label in detected_labels['Labels']:
    #     if label['Name'] == "Person" and label['Confidence'] > 80:
    #         print("Not food")
    #         break
    #     if label['Name'] == "Food":
    #         print(label['Name'] + ' : ' + str(label['Confidence']))
