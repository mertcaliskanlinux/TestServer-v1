from django.contrib import admin
from .models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'title', 'completed','is_archived','created_at', 'updated_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'slug', 'completed', 'created_at', 'updated_at')
        }),
        ('Archived', {
            'fields': ('is_archived',)
        })
    )
    actions = ['mark_completed', 'mark_incomplete', 'archive_items', 'unarchive_items']

    def mark_completed(self, request, queryset):
        rows_updated = queryset.update(completed=True)
        self.message_user(request, f"{rows_updated} ToDo öğesi tamamlandı olarak işaretlendi.")

    def mark_incomplete(self, request, queryset):
        rows_updated = queryset.update(completed=False)
        self.message_user(request, f"{rows_updated} ToDo öğesi tamamlanmamış olarak işaretlendi.")

    def archive_items(self, request, queryset):
        rows_updated = queryset.update(is_archived=True)
        self.message_user(request, f"{rows_updated} ToDo öğesi arşivlendi.")

    def unarchive_items(self, request, queryset):
        rows_updated = queryset.update(is_archived=False)
        self.message_user(request, f"{rows_updated} ToDo öğesi arşivden çıkarıldı.")


    mark_completed.short_description = "Seçilen ToDo öğelerini tamamlandı olarak işaretle"
    mark_incomplete.short_description = "Seçilen ToDo öğelerini tamamlanmamış olarak işaretle"
    archive_items.short_description = "Seçilen ToDo öğelerini arşivle"
    unarchive_items.short_description = "Seçilen ToDo öğelerini arşivden çıkar"


admin.site.register(TodoItem, TodoItemAdmin)
