from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Community, Forum, Profile, Post, Answer, Search, Review, LearningPath, PathStep
from .serializers import CommunitySerializers, ForumSerializers,  ProfileSerializers, PostSerializers,  AnswerSerializers, SearchSerializers, ReviewSerializers, LearningPathSerializers,  PathStepSerializers 



# Create your views here.
class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializers
    permission_classes = [IsAuthenticated]
    

class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializers
    permission_classes = [IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class LearningPathViewSet(viewsets.ModelViewSet):
    queryset = LearningPath.objects.all() 
    serializer_class =  LearningPathSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class PathStepViewSet(viewsets.ModelViewSet):
    queryset = PathStep.objects.all() 
    serializer_class = PathStepSerializers
    permission_classes = [IsAuthenticated]
