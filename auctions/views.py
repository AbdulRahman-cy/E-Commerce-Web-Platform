from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages


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

@login_required
def index(request):

    listings = Listing.objects.filter(is_active=True)
    user = request.user
    user_likes = user.likes.all()
    #user_likes => querySet
    liked_listings = Listing.objects.filter(likes__in=user_likes)
    
    
    #return index.html
    return render(request, "auctions/index.html", {
                "listings": listings,
                "liked_listings": liked_listings })

@login_required
def toggle_like(request, listing_id):

    if request.method == "POST":
        #I used .first() method to return single model instance
        like = Like.objects.filter(listing_id=listing_id, user_id=request.user.id).first()
        if like:
            like.delete()

            #This is a normal python variable
            liked = False
        else:
            #I1-I need to imporve the code here using error message , Integrity error
            Like.objects.create(user_id=request.user.id, listing_id=listing_id)
            liked = True
        
        like_count = Like.objects.filter(listing_id=listing_id).count()

        return JsonResponse({
        'liked': liked,
        'count': like_count
    })

@login_required
def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    user = request.user
    user_likes = user.likes.all()
    liked_listings = Listing.objects.filter(likes__in=user_likes)

    comments = Comment.objects.filter(listing_id = listing_id)
    comments_count = comments.count()

    watchlists = Watchlist.objects.all()
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
        content = request.POST["comment"]
        
        listing = get_object_or_404(Listing, pk=listing_id)
        
        #Adding to db
        try:
            Comment.objects.create(user=request.user, listing=listing, content=content)
        except IntegrityError:
            #I2- I think i should change render to redirect with django error messages
            return render(request, "listing.html", {
                "message": "Error Cannot upload comments"
            })
        
        return redirect("listing", listing_id=listing_id)
    
#I4- watchlist function gets activated when triggered from several routes so should i include the "listing_id as a parameter"
@login_required
def watchlist(request):
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
        
       

    
        
        
        
        



