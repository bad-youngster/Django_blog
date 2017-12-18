from django.contrib import admin

class DeleteAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):

        obj.delete()