from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from mpook.models import *
from mpook.serializers import *

class AllSerializersQuickTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='Otay', password='mokk2')
        self.comm = Community.objects.create(name='برمجة')
        self.forum = Forum.objects.create(community=self.comm, name_forum='باك أند')
        self.profile = Profile.objects.create(user=self.user, primary_forum=self.forum, level='Senior')
        self.profile.joined_forums.add
        self.post = Post.objects.create(profile=self.profile, user=self.user, address='Django Guide', query='a'*100)
        self.answer = Answer.objects.create(post=self.post, user=self.user, content='a'*100, link_answer='https://safe.com')
        self.search = Search.objects.create(community=self.comm, user=self.user, title='API', abstract='Full abstract')
        self.review = Review.objects.create(search=self.search, review_text='Right', user=self.user)
        self.path = LearningPath.objects.create(community=self.comm, title='Backend Path', description='easy learn', user=self.user)
        self.step = PathStep.objects.create(path=self.path, search=self.search, order=1)
        

        factory = APIRequestFactory()
        request = factory.get('/')
        request.user = self.user
        self.context = {'request': request}

    def test_all_serializers_serialization(self):

        cases = [
           (self.comm, CommunitySerializers),
           (self.forum, ForumSerializers),
           (self.profile, ProfileSerializers),
           (self.post, PostSerializers),
           (self.answer, AnswerSerializers), 
           (self.search, SearchSerializers),
           (self.review, ReviewSerializers),
           (self.path, LearningPathSerializers),
           (self.step, PathStepSerializers)
        ]

        for obj, SerializerClass in cases:
            serializer = SerializerClass(instance=obj, context=self.context)
            
            self.assertIsNotNone(serializer.data)

    def test_validation_logic(self):
        invalid_answer_data = {
            'post': self.post.id, 
            'content': 'a'*100,
            'link_answer': 'http://unsafe.com'
        }

        serializer = AnswerSerializers(data=invalid_answer_data, context=self.context)
        self.assertFalse(serializer.is_valid())
        
        invalid_post_data = {
            'profile': self.profile.id,
            'address': 'Short',
            'query': 'Short Querty'
        }
        
        post_serializer = PostSerializers(data=invalid_post_data, context=self.context)
        self.assertFalse(post_serializer.is_valid())





