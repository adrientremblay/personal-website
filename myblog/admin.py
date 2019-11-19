from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from mezzanine.pages.admin import PageAdmin
from .models import MyBlogPage
# from .models import MyPost

# Injecting field into blogadmin

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "tagline")

class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)

# Regestering custom page to pageadmin

admin.site.register(MyBlogPage, PageAdmin)
# admin.site.register(MyPost, BlogPostAdmin)
