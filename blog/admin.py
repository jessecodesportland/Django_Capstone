#Jesse Fitzjarrell 9-30-15
#Blatent copying of Django Girls blog with some minor modifications. 
#I did this to learn Django and prove that I can follow a code example
# I added a jQuery hide show on the comment section and changed the CSS 
from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)