from turtle import title
from django.contrib import admin
from . models  import MyTodo
# Register your models here.
@admin.register(MyTodo)
class MyTodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete', 'created']
    list_filter = ['complete', 'created']
    readonly_fields = ['created']