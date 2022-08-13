from django.contrib import admin
from .models import logo, quotes, Logoimage, Dailyquotes

# Register your models here.
admin.site.register(logo)
admin.site.register(quotes)
admin.site.register(Logoimage)
admin.site.register(Dailyquotes)
