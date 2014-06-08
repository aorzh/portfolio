from django.db import models
from django.contrib import admin
from image_cropping import ImageRatioField
from image_cropping import ImageCroppingMixin


class Page(models.Model):
    title = models.CharField('Title', max_length=150)
    body = models.TextField('Description')
    time = models.DateTimeField('Date')
    image = models.ImageField('Picture', upload_to='pro_images', blank=True)
     # size is "width x height"
    cropping = ImageRatioField('image', '430x360', size_warning=True)

    class Meta:
        ordering = ("-time",)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title


class PageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
    list_display = ("title", "time")
