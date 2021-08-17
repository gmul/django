from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.manager import Manager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag is applidd to what object
    tag = models.ForeignKey(Tag, on_delete=CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE)
    object_id = models.PositiveIntegerField()
    object_type = (GenericForeignKey)


                          
