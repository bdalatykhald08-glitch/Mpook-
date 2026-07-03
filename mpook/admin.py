from django.contrib import admin
from django.contrib.auth.models import User
from .models import Community, Forum, Profile, Post, Answer,  Search, Review,  LearningPath, PathStep

# Register your models here.

admin.site.register(Community)
admin.site.register(Forum)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Search)
admin.site.register(Review)
admin.site.register(LearningPath)
admin.site.register(PathStep)




