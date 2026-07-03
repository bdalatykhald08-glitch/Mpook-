from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='المجتمع')

    class Meta:
        verbose_name = 'المجتمع'
        verbose_name_plural = 'المجتمعات'

    def __str__(self):
        return self.name


class Forum(models.Model):
    community = models.ForeignKey(Community, on_delete=models.PROTECT, related_name='forum_community', verbose_name='المجتمع التابع له')
    name_forum = models.CharField(max_length=150, verbose_name='أسم المنتدي')

    class Meta:
        verbose_name = 'منتدي'
        verbose_name_plural = 'المنتديات'
        unique_together = ('community', 'name_forum')
        ordering = ['community', 'name_forum']

    def __str__(self):
        
        return  f"{self.community.name} -> {self.name_forum}"

    
class Profile(models.Model):
    
    LEVEL_CHOICES = [
        ('Junior', 'مبتديء'),
        ('Senior', 'محترف')
    ]
     
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
    primary_forum = models.ForeignKey(Forum, on_delete=models.PROTECT, null=True, related_name='specialist_profile', verbose_name='التخصص')
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, verbose_name='المستوي')
    joined_forums = models.ManyToManyField(Forum, blank=True, related_name='joined_forums', verbose_name='المنتديات المنضم اليها')
    portfolio_url = models.URLField(max_length=500, blank=True,  null=True, verbose_name='معرض ألاعمال')
    bio_headline = models.CharField(max_length=200, blank=True, null=True, verbose_name='وصف لي أهم أنجازاتك')
    

    class Meta:
        verbose_name = "ملف الشخصي"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        forum_name = self.primary_forum.name_forum if self.primary_forum else 'بدون تخصص'
        return f"{self.user.username} - {self.get_level_display()} ({forum_name})"
    

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profile_post')
    address = models.CharField(max_length=75, verbose_name='عنوان')
    query = models.TextField(verbose_name='ألسؤال')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='كاتب',  related_name='user_post')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"منشور: {self.address[:30]} بواسطة {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']

        verbose_name = 'منشور'
        verbose_name_plural = 'المنشورات'


class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_answer')
    content = models.TextField(verbose_name='ألاجابة')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='كاتب',  related_name='user_answer')
    created_at = models.DateTimeField(auto_now_add=True)
    link_answer = models.URLField(verbose_name='رابط')
    
    def __str__(self):
        return f" إجابة بواسطة {self.user.username} علي {self.post.address[:20]}"

    class Meta:
        ordering = ['-created_at']
        
        verbose_name = 'اجابة'
        verbose_name_plural = 'الأجابات'


class Search(models.Model):
    community = models.ForeignKey(Community, on_delete=models.PROTECT, related_name='community_search', verbose_name='بحوث المجتمع')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='باحث', related_name='user_search')
    title = models.CharField(max_length=55, verbose_name='عنوان البحث')
    abstract = models.TextField(verbose_name='البحث بالكامل')
    seeker_note = models.CharField(max_length=300, blank=True, null=True, verbose_name='ملاحظة الباحث')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='نشرت')


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
    verbose_name = "بحث"
    verbose_name_plural = "الابحاث"
    

    @property
    def mpook_share_link(self):
        return f"https://mpook.com/search/{self.id}/"


class Review(models.Model):
    search = models.ForeignKey(Search, on_delete=models.PROTECT, related_name='search_review')
    review_text = models.TextField(verbose_name='المراجعة')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_review')
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True, verbose_name='المؤيدون')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"مراجعة من {self.user.username} علي {self.search.title}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'مراجعة'
        verbose_name_plural = 'مراجعات'


class LearningPath(models.Model):
    community = models.ForeignKey(Community, on_delete=models.PROTECT, related_name='community_learningpath', verbose_name='المجتمع التابع له')
    title = models.CharField(max_length=100, verbose_name='عنوان مسار التعلم')
    description = models.TextField(verbose_name='وصف المسار')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_learningpath', verbose_name='صاحب المسار')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name = 'مسار التعلم'
        verbose_name_plural = 'مسارات التعلم'


class PathStep(models.Model):
    path = models.ForeignKey(LearningPath, on_delete=models.PROTECT, related_name='learningpath_pathstep', verbose_name='المسار')
    search = models.ForeignKey(Search, on_delete=models.PROTECT, verbose_name='البحث المرتبط بهذه الخطوة')
    order = models.PositiveIntegerField(verbose_name='ترتيب الخطوة')
    
    class Meta:
        ordering = ['order']
        unique_together = ('path', 'order')
        verbose_name = 'خطوة في المسار'
        verbose_name_plural = 'خطوات المسار'

    def __str__(self):
        return f"الخطوة {self.order} في مسار: {self.path.title}"



