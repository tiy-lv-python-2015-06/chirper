import json
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from updates.models import Chirp


class ChirpApiTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="jeff", password="password",
                                   email="jeff@example.com")
        chirp = Chirp.objects.create(title="Test Chirp1", author=self.user,
                                     message="Testing a chirp")
        chirp = Chirp.objects.create(title="Test Chirp2", author=self.user,
                                     message="Testing a chirp")

    def test_get_single_chirp(self):
        chirp = Chirp.objects.first()
        response = self.client.get(reverse('api_chirp_detail', args=[chirp.id]))
        self.assertContains(response, "Chirp1")

    def test_chirp_list(self):
        response = self.client.get(reverse('api_chirp_list'))
        data = json.loads(response.content.decode("utf-8"))
        self.assertContains(response, "Chirp1")
        self.assertContains(response, "Chirp2")

    def test_create_chirp(self):
        response = self.client.post()