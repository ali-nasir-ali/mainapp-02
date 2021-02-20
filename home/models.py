from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    template = "home/home_page.html"
    #max_count = 1

    banner_title = models.CharField(max_lenth=100, blank=False, null=True,)
    content_panel = Page.content_panels + [
         FieldPanel("banner_title")
    ]    

    class Meta:
         verbose_name = "Home Page"
         verbose_name_plural = "Home Pages"