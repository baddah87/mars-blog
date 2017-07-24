from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "author"]
	search_fields = ["title", "author", "content"]
	list_display_link = ["author"]
	list_editable =["author"]

	class Mets:
		model = Post



# Register your models here.
admin.site.register(Post, PostModelAdmin)