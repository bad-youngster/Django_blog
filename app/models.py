from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(u"title",max_length=256)
    content = models.TextField(u"file")

    pub_date = models.DateField(u"start date",auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u"update time",auto_now_add=True,null=True)
    def __str__(self):
        return self.title
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
    full_name = property(my_property)

