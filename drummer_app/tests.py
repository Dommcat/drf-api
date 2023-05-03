from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Drummer


class Drummer_appTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = get_user_model().objects.create_user(username='user1', email='user1@gmail.com', password='1234')
        user1.save()

        test_drummer = Drummer.objects.create(
            name = 'Ringo Starr',
            genre = 'Rock',
            drum_brand = 'Ludwig',
        )
        test_drummer.save()


    # name = models.CharField(max_length=100)
    # band = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # drum_brand = models.CharField(max_length=100)
    # genre = models.CharField(max_length=100)
    # active = models.BooleanField(default=False)   
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


    def test_drummer_content(self):
        drummer = drummer.objects.get(id=1)
        actual_name = str(drummer.name)
        actual_drum_brand = str(drummer.drum_brand)
        actual_genre = str(drummer.genre)
        self.assertEqual(actual_name, 'Ringo Star')
        self.assertEqual(actual_drum_brand, 'Ludwig')
        self.assertEqual(actual_genre, 'Rock')

# Create your tests here.
