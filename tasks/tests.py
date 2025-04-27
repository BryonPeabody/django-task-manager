from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class TaskTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_task_list_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('task-list'))
        self.assertRedirects(response, '/tasks/login/?next=/tasks/')

    def test_task_list_loads_for_logged_in_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Task')

    def test_create_task(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create-task'), {
            'title': 'Test Task',
            'description': 'Test Description',
            'is_complete': False
        })
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'Test Task')
