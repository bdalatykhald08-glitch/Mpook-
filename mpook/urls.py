from django.urls import  path, include
from .views import  CommunityViewSet, ForumViewSet, ProfileViewSet,  PostViewSet, AnswerViewSet, SearchViewSet, ReviewViewSet, LearningPathViewSet, PathStepViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'communities', CommunityViewSet, basename='community'),
router.register(r'Forums', ForumViewSet, basename='Forum_Field'),
router.register(r'profiles', ProfileViewSet, basename='profile_info'),
router.register(r'posts', PostViewSet, basename='post_info'),
router.register(r'answers', AnswerViewSet, basename='answer_list'),
router.register(r'searches', SearchViewSet, basename='search_list'),
router.register(r'reviews', ReviewViewSet, basename='review_note'),
router.register(r'learning_paths', LearningPathViewSet, basename='learn_path'),
router.register(r'pathsteps', PathStepViewSet, basename='pathst')


urlpatterns = [
    path('', include(router.urls)), 
    
]
