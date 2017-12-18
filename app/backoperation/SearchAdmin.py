from django.contrib import admin
#  search 'name','age' key
class PersonAdmin1(admin.ModelAdmin):
    list_display1 = ('name','age')
    search_fields1 = ('name')
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct = super(PersonAdmin1,self).get_search_results(request,queryset,search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term)
        except:
            pass
        return  queryset,use_distinct