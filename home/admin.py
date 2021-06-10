from django.contrib import admin
from .models import Home,About,profile,category,Skills,portfolio
#from portfolio.home.models import Home

# Register your models here.
admin.site.register(Home)


# About
class profileinline(admin.TabularInline):
    model= profile
    extra=2 


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines=[
        profileinline,
    ]

# Skills

class Skillsinline(admin.TabularInline):
    model=Skills
    extra=2

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    inlines=[
        Skillsinline,
    ]
#portfolio

admin.site.register(portfolio)