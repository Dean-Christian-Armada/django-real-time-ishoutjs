from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _

from . models import *

# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
	fieldsets = (
		(None, {'fields': ('url', 'title', 'content', 'sites')}),
		(_('Advanced options'),{
			'classes': ('collapse', ),
			'fields': (
				'enable_comments',
				'registration_required',
				'template_name',
			),
		}),
	)

# Register your models here.
admin.site.register(TaggedItem)
admin.site.register(BookMark)
admin.site.register(Name)

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)