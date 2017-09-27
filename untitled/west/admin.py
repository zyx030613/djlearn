from django.contrib import admin
from west.models import Character, Contact, Tag
#admin.site.register([Character, Contact, Tag])

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag





class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    fieldsets = (
        ['Main',{
            'fields':('name', 'email'),
        }],
        ['Advance',{
            'classes':('collapse', ),
            'fields':('age',),
        }]
    )
    list_display = ('name','age','email')
    search_fields = ('name',)
admin.site.register(Contact,ContactAdmin)
admin.site.register([Character])