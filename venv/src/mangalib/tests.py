from django.test import TestCase
from .models import Author

# Create your tests here.
class AuthorTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Athanase Alcide")
    
    def test_iscorrect_instance(self):
        self.assertIsInstance(self.author, Author)
        
    def test_exist(self):
        author = Author.objects.create(pk= 1)
        self.asserTrue(author)