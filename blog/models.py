from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on '{self.post.title}'"
