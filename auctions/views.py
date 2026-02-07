from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.views.decorators.cache import never_cache


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

    
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@never_cache
@login_required
def index(request):
    #Needs mod here
    categories=Category.objects.filter(is_selected=True)
    listings = Listing.objects.filter(is_active=True, category__in=categories)
    user = request.user
    user_likes = user.likes.all()
    #user_likes => querySet
    liked_listings = Listing.objects.filter(likes__in=user_likes)

    watchlists = Watchlist.objects.filter(user=user)
    watchlist = Listing.objects.filter(watchlists__in=watchlists)
    

    
    #return index.html
    return render(request, "auctions/index.html", {
                "listings": listings,
                "liked_listings": liked_listings,
                "watchlist": watchlist })

@login_required
def toggle_like(request, listing_id):

    if request.method == "POST":

        listing = get_object_or_404(Listing, pk=listing_id)
        like, created = Like.objects.get_or_create(listing=listing, user=request.user)

        if not created:
            like.delete()
        
            liked = False
        else:
            liked = True
        
        like_count = Like.objects.filter(listing_id=listing_id).count()

        return JsonResponse({
        'liked': liked,
        'count': like_count
    })

@never_cache
@login_required
def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    user = request.user
    user_likes = user.likes.all()
    liked_listings = Listing.objects.filter(likes__in=user_likes)

    comments = Comment.objects.filter(listing_id = listing_id)
    comments_count = comments.count()

    watchlists = Watchlist.objects.filter(user=user)
    watchlist = Listing.objects.filter(watchlists__in=watchlists)

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "liked_listings":liked_listings,
        "comments": comments,
        "comments_count": comments_count,
        "watchlist": watchlist
    })      

@login_required
def comment(request, listing_id):
    if request.method == "POST":
        #This means if no content return an empty string
        content = request.POST.get("comment", "").strip()

        if not content:
            messages.error(request, "Comment cannot be empty")
            return redirect("listing", listing_id=listing_id)
        
        listing = get_object_or_404(Listing, pk=listing_id)
        
        try:
            Comment.objects.create(
                user=request.user, 
                listing=listing, 
                content=content
            )
            messages.success(request, "Comment added successfully")
        except Exception as e:
            messages.error(request, "Failed to add comment")
        
        return redirect("listing", listing_id=listing_id)
    
    return redirect("listing", listing_id=listing_id)
    
@login_required
def watchlist_toggle(request):
    if request.method == "POST":
        #I3- Reacll request envelope yabni process (key=value) pairs is in the body
        
        listing_id = request.POST["listing"]

        watchlist = Watchlist.objects.filter(user=request.user, listing_id=listing_id)
        if watchlist:
            watchlist.delete()
            messages.success(request, "Removed from watchlist")
        else:
            try:
                Watchlist.objects.create(user=request.user, listing_id=listing_id)
            except IntegrityError:
                messages.error(request, "Cannot add to watchlist")
            messages.success(request, "Added to watchlist")
        return redirect(request.META.get('HTTP_REFERER', 'index'))
    
@login_required
def watchlist_view(request):
    
    user = request.user
    user_likes = user.likes.all()

    liked_listings = Listing.objects.filter(likes__in=user_likes)

    watchlists = Watchlist.objects.filter(user=user)

    watchlist = Listing.objects.filter(watchlists__in=watchlists)

    listings = Listing.objects.filter(is_active=True, watchlists__in=watchlists)
    
    return render(request, "auctions/index.html", {
                "listings": listings,
                "liked_listings": liked_listings,
                "watchlist": watchlist
                 })

@login_required
def categories(request):

    if request.method == "POST":

        raw = request.POST.get("selected_categories")

        if raw:
            selected_ids = raw.split(",")
        else:
            selected_ids = []

        # reset all categories
        Category.objects.update(is_selected=False)

        # mark only selected ones
        if selected_ids:
            Category.objects.filter(id__in=selected_ids).update(is_selected=True)

        messages.success(
            request,
            "Displayed listings are based on your category selection"
        )

        return redirect("index")

    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })



        
    
    
        
       

    
        
        
        
        



