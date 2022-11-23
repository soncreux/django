from django.db import models
from django.utils.html import escape

from django.core.validators import MinValueValidator, MaxValueValidator


from django.db import models
from django.utils.html import escape, mark_safe


class Post(models.Model):

    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{https://hi-news.ru/wp-content/uploads/2022/03/crypto_history_image_two-750x429.jpg}" width="300" height="300" />'.format(self.thumbnail.url))
        return ""
    
    
    
    
    
    #def image_tag(self):
    
        #return u'<img src="%s" />' % escape(https://media2.nekropole.info/2020/07/Artur-Sherbius.jpg)
    #image_tag.short_description = 'Image'
    #image_tag.allow_tags = True


 