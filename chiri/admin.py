from django.contrib import admin
from .models import logo, quotes, Logoimage, Dailyquotes, Videolink, Addsimage, Engmemes

# Register your models here.
admin.site.register(logo)
admin.site.register(quotes)
admin.site.register(Logoimage)
admin.site.register(Dailyquotes)
admin.site.register(Videolink)
admin.site.register(Addsimage)
admin.site.register(Engmemes)