from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title','slug','status','created_on','updated_on')
    list_filter = ('status',)
    search_fields = ('title','content')
    prepopulated_fields = {'slug':('title',)}
    


