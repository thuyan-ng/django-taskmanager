from django.test import TestCase
from .models import Developer
from django.shortcuts import reverse

class ModelClass(TestCase):

    def setUp(self):
        Developer.objects.create(first_name="Sebastien", last_name="Drobisz")

    def test_is_free_with_no_tasks(self):
        dev = Developer.objects.get(first_name="Sebastien")
        self.assertIs(dev.is_free(), True)

    def test_is_free_with_one_task(self):
        dev = Developer.objects.get(first_name="Sebastien")
        dev.tasks.create(title="Cours Django", description="Faire le cours sur Django")
        self.assertIs(dev.is_free(), False)

class DeveloperIndexViewTests(TestCase):
    def test_no_developers(self):
        response = self.client.get(reverse('developer:index'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Il n'y a aucun dévelopeur enregistré!")
        self.assertQuerysetEqual(response.context['developers'], [])

    def test_one_developer(self):
        dev = Developer.objects.create(first_name="Jonathan", last_name="Lechien")
        response = self.client.get(reverse('developer:index'))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context['developers'], [f'<Developer: {dev.first_name} {dev.last_name}>'])
        self.assertContains(response, dev.first_name)

class DevDetailView(TestCase):
    def test_existing_developer(self):
        dev = Developer.objects.create(first_name="Jonathan", last_name="Lechien")
        url = reverse('developer:detail', args=(dev.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['developer'], dev)
        self.assertContains(response, dev.first_name)
        self.assertContains(response, dev.last_name)
    
    def test_non_existing_developer(self):
        url = reverse('developer:detail', args=(1,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)