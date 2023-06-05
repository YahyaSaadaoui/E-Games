from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Game


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(category_name='new', category_slug='new')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'new')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(reverse('store:category_list', args=[data.slug]))
        self.assertEqual(response.status_code, 200)





# Testing the Game Class if it have all the fields inserted correctly ....... 

class TestGamesModel(TestCase):
    def setUp(self):
        Category.objects.create(Name='new', Game_slug='new')
        User.objects.create(username='yahya')
        self.data1 = Game.objects.create(category_id=1, Name='Valorant', created_by_id=1,
                                         game_slug='valorant', Price='0,21', 
                                         image='valorant-listing-800x450_Bevx8yD')
        self.data2 = Game.Games.create(category_id=1, Name='COD', 
                                       created_by_id=1,game_slug='cod',
                                         Price='20.00', 
                                         image='Paranormal_playstation_logo__COD_8f49543f-5cb9-460e-9fed-c7a855decc35.png')

    def test_Games_model_entry(self):
        """
        Test Game model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Game))
        self.assertEqual(str(data), 'Valorant')

    def test_Games_url(self):
        """
        Test Game model slug and URL reverse
        """
        data = self.data1
        url = reverse('store:Game_detail', args=[data.slug])
        self.assertEqual(url, '/item/Valorant/')
        response = self.client.post(
            reverse('store:Game_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_Games_custom_manager_basic(self):
        """
        Test Game model custom manager returns only active Games
        """
        data = Game.Games.all()
        self.assertEqual(data.count(), 1)
