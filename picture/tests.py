from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.

class LocationTestClass(TestCase):
    '''
    test for Location class
    '''

    # Set up method
    def setUp(self):
        self.loc1= Location(country_name = 'Rwanda', city_name ='Kigali')
  
    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.loc1= Location(country_name = 'Rwanda', city_name ='Kigali')
        self.loc1.save_editor()

        # Creating a new tag and saving it
        self.new_cat = Category(Category = 'travel')
        self.new_cat.save()

        self.new_image= Image(image = 'sky.jpeg',title = 'sky dive',description = 'a way to live adventure',location = self.loc1)
        self.new_image.save()

        self.new_image.Category.add(self.new_cat)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
