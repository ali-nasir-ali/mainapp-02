""" Flexible page """
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

class FlexPage(Page):
    template= "flex/flex_page.html"

    # @todo add streamfield
    content = StreamField()

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    content_panels = Page.content_panels +[
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name= "Flex Page"
        verbose_name_plural = "Flex Pages"

