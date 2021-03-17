from django.contrib import admin
from .models import Post
from .models import Candidate

admin.site.register(Post)   
admin.site.register(Candidate)