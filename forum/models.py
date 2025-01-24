from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class ForumPost(models.Model):
    """
    Represents a forum post created by a user.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Saves the forum post instance to the database.
        Automatically generates a unique slug.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ForumComment(models.Model):
    """
    Represents a comment on a forum post.
    """
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
