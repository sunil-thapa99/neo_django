from django.contrib import admin
from .models import Category

'''
	Cheat sheet: https://www.mercurytide.co.uk/media/resources/django-cheat-sheet.pdf
'''

# admin.site.register(Category) => Old style

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	# Field name to be displayed. 
	list_display = ('name', 'slug', 'created', 'updated', 'is_active', )
	date_hierarchy = 'updated'
	list_editable = ('is_active', )
	list_filter = ('created', 'updated', 'is_active', )
	search_fields = ('name', 'slug', )

	# - represents negative order, last action at the top
	ordering = ('-updated', )

	list_per_page = 2
	prepopulated_fields = {'slug': ('name', )}

	def get_list_display(self, request):
		if request.user.is_superuser:
			return ('name', 'slug', 'created', 'updated', 'is_active')
		else:
			return ('name', 'slug', 'updated')