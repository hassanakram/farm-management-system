from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Animal


class AnimalAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.animal = Animal.objects.create(name="Goat")

    def test_get_animals(self):
        response = self.client.get(reverse("animal-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_animal(self):
        data = {"name": "Tiger"}
        response = self.client.post(reverse("animal-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Animal.objects.count(), 2)

    def test_duplicate_name(self):
        Animal.objects.create(name="Lion")

        with self.assertRaises(IntegrityError):
            Animal.objects.create(name="Lion")

    def test_unique_name(self):
        Animal.objects.create(name="Elephant")

        try:
            Animal.objects.create(name="Tiger")
        except IntegrityError:
            self.fail("Creating an animal with a unique name failed unexpectedly.")
