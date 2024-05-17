from django.contrib import admin
from posts.models import Post


from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'user__username')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'user', 'description', 'completed')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            print("request user:", request.user)
            obj.user = request.user
        super().save_model(request, obj, form, change)



