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







