from django.contrib import admin
from .models import Blogs,CommentBlog,HelpMessage

# Register your models here.

admin.site.register(Blogs)
admin.site.register(CommentBlog)
admin.site.register(HelpMessage)

