from django.contrib import admin

class SaveAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            obj_original = self.model.objects.get(pk=obj.pk)
        else:
            obj_original = None
        obj.user = request.user
        obj.save()