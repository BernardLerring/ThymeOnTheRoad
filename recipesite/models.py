from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
CUISINE = ((0, "Italian"), (1, "Indian"), (2, "Chinese"), (3, "Thai"), (4, "American"), (5, "Mexican"), (6, "Middle Eastern"), (7, "Miscellaneous"))


class Recipe (models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    ingredients = tinymce_models.HTMLField()
    method = tinymce_models.HTMLField(null=True, blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cuisine = models.IntegerField(choices=CUISINE, default=0)
    likes = models.ManyToManyField(User, related_name="recipe_likes", blank=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment (models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"



