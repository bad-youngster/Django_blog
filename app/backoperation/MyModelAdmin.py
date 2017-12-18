from django.contrib import admin
#if login user is superuser can look all,else user only look users
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return  qs.filter(author = request.user)