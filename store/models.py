
from django.conf import settings
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255, db_index=True)
    category_slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Game(models.Model):
    category = models.ForeignKey(Category, related_name='games', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='games_created', default=None)
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    console_type = models.CharField(max_length=255, db_index=True)
    details = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    game_slug = models.SlugField(max_length=255, unique=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Games'
        ordering = ('-created',)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()

    class Meta:
        unique_together = ('user', 'game')


class Image(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image)

