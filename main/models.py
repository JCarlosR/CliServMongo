from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mongoengine import *

class Language(EmbeddedDocument):
	name = StringField(max_length=100)

class Developer(Document):
    name = StringField(max_length=200)
    years = IntField(min_value=0)
    register_date = DateTimeField(help_text='registered date')
    languages = ListField(EmbeddedDocumentField(Language))
    area = StringField(max_length=200)

    @property
    def slug(self): 
		return self.name.replace(" ", "_")

class Area(Document):
    name = StringField(max_length=200)
    