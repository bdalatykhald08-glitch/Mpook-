from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class CommunityTest(APITestCase):
    def test_get_all_communities(self):
        
        url = reverse('community-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ForumTest(APITestCase):
    def test_get_nameforum(self):

        url = reverse('forum-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProfileTest(APITestCase):
    def test_create_profile(self):       
        
        url = reverse('profile-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PostTest(APITestCase):
    def test_create_post(self):
        
        url = reverse('post-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AnswerTest(APITestCase):
    def test_create_answer(self):

        url = reverse('answer-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class SearchTest(APITestCase):
    def test_look_search(self):
        
        url = reverse('search-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ReviewTest(APITestCase):
    def test_create_review(self):
        
        url = reverse('forum-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LearningPathTest(APITestCase):
    def test_get_learningpath(self):
        
        url = reverse('forum-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PathStepTest(APITestCase):
    def test_link_pathstep(self):

        url = reverse('forum-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)






















