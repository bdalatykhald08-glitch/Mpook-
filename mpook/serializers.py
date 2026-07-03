from rest_framework import serializers
from .models import  Community, Forum, Profile, Post, Answer, Search, Review, LearningPath, PathStep

class CommunitySerializers(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ['id', 'name']
    

class ForumSerializers(serializers.ModelSerializer):

    class Meta:
        model = Forum
        fields = ['id', 'community', 'name_forum']


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'primary_forum', 'level', 'joined_forums', 'portfolio_url', 'bio_headline']
        read_only_fields = ['user']


    def validate_joined_forums(self, value):
         
        if not value:
            raise  serializers.ValidationError("يجب أن تنضم لمنتدي واحد علي ألاقل")

        if len(value) > 3:
            raise serializers.ValidationError("لايمكنك التسجيل في أكثر من ثلاث منتديات")
        
        profile = self.instance
        if profile and profile.primary_forum:
            current_community = profile.primary_forum.community
            for forum in value:
                if current_community != forum.community:
                    raise serializers.ValidationError(f" المنتدي{forum.name_forum} ليس جزاء من مجتمعك الحالي ")
        return value

    def validate(self, attrs):
        portfolio_url = attrs.get('portfolio_url')
        bio_headline = attrs.get('bio_headline')
        level = attrs.get('level')

        if level == 'Senior':
            if not portfolio_url:
               raise serializers.ValidationError({"portfolio_url": "بما أنك محترف قدم لنا رابط معرض أعمالك مثل لينكد أن أو منصة لعرض ألاعمال "})
        
            if not bio_headline:
                raise serializers.ValidationError({"bio_headline": "يرجي كتابة وصف لأهم أنجازتك"})
        return attrs
    
class PostSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'profile', 'address', 'query', 'user','created_at']
        read_only_fields = ['created_at', 'user']
    
    def validate_query(self, value):
        if len(value) < 100:
            raise serializers.ValidationError("لايسمح بكتابة أقل من 100 حرف لسؤال")
        return value

class AnswerSerializers(serializers.ModelSerializer):
    link_answer = serializers.URLField()

    class Meta:
        model = Answer
        fields = ['id', 'post', 'content', 'user', 'link_answer', 'created_at']
        read_only_fields = ['created_at', 'user']

    def validate_content(self, value):
        if len(value) < 100:
           raise serializers.ValidationError("لايمكن وضع أجابة أقل من 100 حرف")
            
        return value

    def validate_link_answer(self, value):
        if 'https' not in value:
            raise serializers.ValidationError("الرابط غير آمن لضمان ألأمان يجب وضع الرابط بصيغة https")
        return value
        
    
class SearchSerializers(serializers.ModelSerializer):
    
    
    class Meta:
        model = Search
        fields = ['id', 'community', 'user', 'title', 'abstract', 'seeker_note', 'created_at', 'updated_at', 'is_published']
        read_only_fields = ['created_at', 'updated_at', 'user']

   
    def validate(self, attrs):
        title = attrs.get('title')
        abstract = attrs.get('abstract')
        community = attrs.get('community')

        if not community:
            raise serializers.ValidationError("لايوجد بحث خارج المجتمع")
        
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            seeker_user = getattr(request.user, 'seeker_user', None)
            if not seeker_user or seeker_user.level != 'Senior':
                raise serializers.ValidationError("من يقوم بعمل البحث فقط المحترف ")
        else:
            raise serializers.ValidationError("يجب تسجيل الدخول أولا")
        return attrs
    

class ReviewSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['id', 'review_text', 'created_at', 'search', 'user', 'likes']
        read_only_fields = ['created_at', 'user']

    
    def validate_review_text(self, value):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user_profile = getattr(request.user, 'user_profile', None)
            if not user_profile or user_profile.level != 'Senior':
                raise serializers.ValidationError("المراجعة  يقوم بعملها المحترف فقط")
            else:
                raise serializers.ValidationError("يجب التسجيل أولا")
        return value

class LearningPathSerializers(serializers.ModelSerializer):

    class Meta:
        model = LearningPath
        fields = ['id', 'community', 'title', 'description', 'user', 'created_at']
        read_only_fields = ['created_at', 'user']

    def validate(self, attrs):
        community = attrs.get('community')
        title = attrs.get('title')

        if not title:
            raise serializers.ValidationError({"title":  "عنوان المسار مطلوب لايمكن وضعه فارغا"})
        
        if not community:
            raise serializers.ValidationError({"community": "يجب تحديد المجتمع التابع له المسار"})
        
        return attrs
    
class PathStepSerializers(serializers.ModelSerializer):

    class Meta:
        model = PathStep
        fields = ['id', 'path', 'search', 'order']

    def validate(self, attrs):
        path = attrs.get('path')
        search = attrs.get('search')
        if path and search:
            if path.community != search.community:
                raise serializers.ValidationError("خطاء: لايمكن أضافة هذا البحث لأن المجتمع التابع له المسار يختلف عن مجتمع المسار الحالي")
        return attrs
    


    