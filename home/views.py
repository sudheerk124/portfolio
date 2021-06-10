from django.shortcuts import render,HttpResponse
from .models import Home,category, Skills, portfolio, About,profile


def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles= profile.objects.filter(about=about)

    #category
    categories = category.objects.all()

    #portfolio
    portfolios = portfolio.objects.all()


    context ={
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }


    return render(request,'index.html',context)