from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)
    image_url = models.URLField(blank=True)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name="listings")
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="listings")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="likes")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "listing"],
                name="unique_like"
            )
        ]
    
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comments")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

class Watchlist(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="watchlist")
     listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="watchlists")
     
     class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "listing"],
                name="unique_watchlist"
            )
        ]

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "listing"],
                name="unique_user_listing_cart"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.listing} ({self.quantity})"

