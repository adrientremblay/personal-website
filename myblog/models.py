from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.blog.models import BlogPost
from mezzanine.core import fields

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.

class MyBlogPage(Page, RichText):
    tagline = models.TextField()
    cover = fields.FileField("Image", upload_to="dir/", format="Image");

# class MyPost(BlogPost):
#     tagline = models.TextField()
