from django.contrib import admin
from .models import Account, Contact, Relation
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class AccountResource(resources.ModelResource):
    class Meta:
        model = Account

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class RelationResource(resources.ModelResource):
    class Meta:
        model = Relation

class AccountAdmin(ImportExportActionModelAdmin):
    resource_class = AccountResource

class ContactAdmin(ImportExportActionModelAdmin):
    resource_class = ContactResource

class RelationAdmin(ImportExportActionModelAdmin):
    resource_class = RelationResource

admin.site.register(Account, AccountAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Relation, RelationAdmin)



# admin.py

# from django.contrib import admin
# from .models import JsonData

# class JsonDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'created_at', 'display_table_data')  # Add other fields as needed
#     readonly_fields = ('display_table_data',)

#     def display_table_data(self, obj):
#         # Assuming the JSON data is stored as a list of dictionaries
#         # You can customize this method based on your JSON structure
#         table_html = '<table border="1">'
#         if 'data' in obj:
#             for item in obj['data']:
#                 table_html += '<tr>'
#                 for key, value in item.items():
#                     table_html += f'<td>{key}</td><td>{value}</td>'
#                 table_html += '</tr>'
#         table_html += '</table>'
#         return table_html

#     display_table_data.short_description = 'Table Data'

# admin.site.register(JsonData, JsonDataAdmin)



