from django.test import TestCase
from django.contrib.auth.models import User
from mpook.models import Community, Forum, Profile, Post, Answer, Search, Review, LearningPath, PathStep


class AllModelsQuickTest(TestCase):
    def test_all_models_creation_and_str(self):
        user = User.objects.create_user(username='Otay', password='mook55')
        other_user = User.objects.create_user(username='ReviewUser', password='ook22')

        comm = Community.objects.create(name='برمجة')
        forum = Forum.objects.create(community=comm, name_forum='باك أند')
        
        profile = Profile.objects.create(user=user, primary_forum=forum, level='Junior')
        profile.joined_forums.add(forum)
        post = Post.objects.create(profile=profile, user=user, address='Django guide for beginner', query='test')
        answer = Answer.objects.create(post=post, user=user, content='test answer')

        search = Search.objects.create(community=comm ,user=user, title='API', abstract='how to link between backend and frontend')
        review = Review.objects.create(search=search, user=user, review_text='it is good but you need to know about  other field to link')
        review.likes.add(other_user)
        path = LearningPath.objects.create(community=comm, title='Backend Path', description='Learn Django', user=user)
        step = PathStep.objects.create(path=path, search=search, order=1)
        
        all_objects = [comm, forum, profile, post, answer, search, review, path, step]
        for obj in all_objects:
            self.assertTrue(isinstance(str(obj), str))
            self.assertIsNotNone(obj.pk)












