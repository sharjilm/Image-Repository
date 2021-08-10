from django.conf import settings
from google.cloud import vision
from google.cloud.vision_v1 import types
import os
import cv2
import cvlib as cv
import requests
import numpy as np


# If the Google Vision API credentials are provided in settings, image_detect will use the API to provide tag suggestions
# for an image based on object detection. If the credentials are not provided it will use the python library 'cvlib' for
# providing these object detection suggestions
# @params image_url: the URL of the image that the object detection will be run on
# @returns suggested_vision_tags: a string of suggested tags for the image based on objects detected in it
def image_detect(image_url):

    # The image_detect function will run the object detection algorithm using the Google Vision API
    try:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        client = vision.ImageAnnotatorClient()

        # If AWS credentials are provided, google image detection will be run on the image URL *
        try:

            settings.AWS_ACCESS_KEY_ID
            settings.AWS_SECRET_ACCESS_KEY
            settings.AWS_STORAGE_BUCKET_NAME

            labels = []
            label_string = ""
            image = types.Image()
            image.source.image_uri = image_url
            response_label = client.label_detection(image=image)
            for label in response_label.label_annotations:
                labels.append(label.description)
            for label in labels:
                if len(label.split()) == 1:
                    label_string += label + ", "

            suggested_vision_tags = label_string.strip(', ')
            return suggested_vision_tags

        # If AWS credentials are not provided, google image detection will be run on the image (local) URL *
        except:

            with open("." + image_url, "rb") as f:
                content = f.read()

            labels = []
            label_string = ""
            response_label = client.label_detection({'content': content, })

            for label in response_label.label_annotations:
                labels.append(label.description)

            for label in labels:
                if len(label.split()) == 1:
                    label_string += label + ", "

            suggested_vision_tags = label_string.strip(', ')

            return suggested_vision_tags

    # As a default, if the vision algorithm cannot be run with the Google Vision API (ex. Google API credentials are not provided),
    # it will be run with the python library 'cvlib.'
    except:
        # If AWS credentials are provided, cvlib image detection will be run on the image URL
        try:

            settings.AWS_ACCESS_KEY_ID
            settings.AWS_SECRET_ACCESS_KEY
            settings.AWS_STORAGE_BUCKET_NAME

            label_string = ""

            resp = requests.get(image_url)

            image = np.asarray(bytearray(resp.content), dtype="uint8")
            img = cv2.imdecode(image, cv2.IMREAD_COLOR)

            bbox, labels, conf = cv.detect_common_objects(img)

            labels = list(set(labels))

            for label in labels:
                if len(label.split()) == 1:
                    label_string += label.capitalize() + ", "

            suggested_vision_tags = label_string.strip(', ')

            return suggested_vision_tags

        # If AWS credentials are not provided, cvlib image detection will be run on the image (local) URL*
        except:

            label_string = ""

            im = cv2.imread("." + image_url)

            bbox, labels, conf = cv.detect_common_objects(im)

            labels = list(set(labels))

            for label in labels:
                if len(label.split()) == 1:
                    label_string += label.capitalize() + ", "

            suggested_vision_tags = label_string.strip(', ')

            return suggested_vision_tags