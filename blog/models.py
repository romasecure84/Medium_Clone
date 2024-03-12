from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Third Party Apps:
from autoslug import AutoSlugField
from tinymce import models as tinymce_models


class CommonModel(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True,)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('title',)


class Category(CommonModel):
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'blog:category_view',
            kwargs={
                'category_slug': self.slug
            }
        )


class Tag(CommonModel):
    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse(
            'blog:tag_view',
            kwargs={
                'tag_slug': self.slug
            }
        )
    


class BlogPost(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    cover_image = models.ImageField(upload_to='post')
    content = tinymce_models.HTMLField(blank=True, null=True)
    view_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse(
            'read:post_detail_view',
            kwargs={
                "user_slug": self.user.profile.slug,
                "post_slug": self.slug,
            }
        )


class UserPostFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)