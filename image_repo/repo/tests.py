#from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from .models import Image, History

# Includes test cases to check user's id value, username, and email.
class UsersTestCase(unittest.TestCase):
    def test_first_user(self):
        user = User.objects.first()
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'sharjilm')
        self.assertEqual(user.email, 'sharjilmohsin@gmail.com')
    
    def test_second_user(self):
        user = User.objects.last()
        self.assertEqual(user.id, 2)
        self.assertEqual(user.username, 'TestUser')
        self.assertEqual(user.email, '')

# Includes test cases to check the image's title, image file name, the tags created by Google Cloud Vision API
# and the username of the uploader.
class ImagesTestCase(unittest.TestCase):
    def test_first_image(self):
        image = Image.objects.first()
        self.assertEqual(image.title, 'Pacman')
        self.assertEqual(image.imageName, 'pacman.jpeg')
        self.assertEqual(image.vision_tags, 'None')
        self.assertEqual(image.uploader.username, 'sharjilm')
    
    def test_last_image(self):
        image = Image.objects.last()
        self.assertEqual(image.title, 'Lamborghini')
        self.assertEqual(image.imageName, 'lamborghini.jpg')
        self.assertEqual(image.vision_tags, 'Car')
        self.assertEqual(image.uploader.username, 'sharjilm')

# Includes test cases to check the history log's username of the uploader of image, the title of the image,
# the image file name, and whether it was uploaded or deleted.
class HistorysTestCase(unittest.TestCase):
    def test_first_history(self):
        history = History.objects.first()
        self.assertEqual(history.user, 'sharjilm')
        self.assertEqual(history.title, 'Lamborghini')
        self.assertEqual(history.name, 'lambourghini.jpg')
        self.assertEqual(history.action, 'uploaded')
        
    def test_last_history(self):
        history = History.objects.last()
        self.assertEqual(history.user, 'sharjilm')
        self.assertEqual(history.title, 'Lamborghini')
        self.assertEqual(history.name, 'lambourghini.jpg')
        self.assertEqual(history.action, 'uploaded')
