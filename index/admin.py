from django.contrib import admin

# Register your models here.

from .models import *

class FormAdmin(admin.ModelAdmin):
    list_display= ('id','code', 'title', 'description', 'creator')

class UserAdmin(admin.ModelAdmin):
    list_display= ('id','username','email', 'password', 'is_superuser', 'first_name', 'is_staff','last_login')

class DistrictAdmin(admin.ModelAdmin):
    list_display= ('id','name')
class TalukaAdmin(admin.ModelAdmin):
    list_display= ('id','name','district_id')

class BlockAdmin(admin.ModelAdmin):
    list_display= ('id','name','taluka_id')
class SectorAdmin(admin.ModelAdmin):
    list_display= ('id','name', 'block_id')

class VillageAdmin(admin.ModelAdmin):
    list_display= ('id','name', 'sector_id')
   
class AwcAdmin(admin.ModelAdmin):
    list_display= ('id','name','sector_id','village_id')

admin.site.register(User,UserAdmin)

admin.site.register(District,DistrictAdmin)
admin.site.register(Taluka,TalukaAdmin)
admin.site.register(Block,BlockAdmin)
admin.site.register(Sector,SectorAdmin)
admin.site.register(Village,VillageAdmin)
admin.site.register(AWC,AwcAdmin)

admin.site.register(Form,FormAdmin)

admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(Responses)



