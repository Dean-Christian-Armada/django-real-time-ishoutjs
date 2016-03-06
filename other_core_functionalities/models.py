from django.contrib.contenttypes.fields import GenericForeignKey # Allows the relationship to be with any model
from django.contrib.contenttypes.fields import GenericRelation # Can be compared as a reversed Foreign key
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.

class TaggedItem(models.Model):
	tag = models.SlugField()
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id') # These 2 are the default fields that the GenericForeignKey will look for

	def __str__(self):
		return self.tag

class BookMark(models.Model):
	url = models.URLField()
	# tags = GenericRelation(TaggedItem, related_query_name='bookmarks')
	# related_query_name enables the foreign key object to create a choice of filter on its dependent field
	tags = GenericRelation(TaggedItem, content_type_field='content_type_fk', object_id_field='object_primary_key')

	def __str__(self):
		return self.url

class Name(models.Model):
	first_name = models.CharField(max_length=100, default=None)
	middle_name = models.CharField(max_length=100, default=None)
	last_name = models.CharField(max_length=100, default=None)

	def __str__(self):
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

class CompanyOwner(models.Model):
	owner = models.ForeignKey(Name)
	name = models.CharField(max_length=50, default=None)

	def __str__(self):
		return "%s" % self.name 