from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>/like/", views.toggle_like, name="toggle_like"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("listing/<int:listing_id>/comment", views.comment, name="comment"),
    path("watchlist_toggle", views.watchlist_toggle, name="watchlist_toggle"),
    path("watchlist", views.watchlist_view, name="watchlist_view"),
    path("category", views.categories, name="categories"),
    path("listing/<int:listing_id>/cart/", views.toggle_cart, name="toggle_cart")
]
