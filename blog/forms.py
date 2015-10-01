#Jesse Fitzjarrell 9-30-15
#Blatent copying of Django Girls blog with some minor modifications. 
#I did this to learn Django and prove that I can follow a code example 
# I added a jQuery hide show on the comment section and changed the CSS 
from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)