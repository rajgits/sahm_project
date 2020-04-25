from django.contrib import admin
from . import models

class userAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','country','city','designation','email')
    search_fields = ('firstname','lastname','country','designation')
    list_filter =('country','work_type')
    #  def get_fields(self, request):
    #      fields = super(SubSectionAdmin, self).get_fields(request, obj)
    #      fields.remove('google_id','facebook_id')
    #      return fields        
     

    # def change_view(self, request, object_id, extra_context=None):
    #     self.exclude = ('google_id','facebook_id','password','address','profile_image','profile_image_verified','company_name','experience_year',
    #     'experience_month','industry_id','full_work_type','part_work_type','fullpart_work_type'
    #     ,'freelance_work_type','fixed_price','perhour_price_currency',
    #     'phoneopt','otpdatetime','emailotp','emailotpstatus',
    #     'registration_date','lastupdate_date','activation_status',
    #     'status','lat','long','is_live','show_map'
    #      )
    #     return super(userAdmin, self).change_view(request, object_id, extra_context)

class categoryAdmin(admin.ModelAdmin):  
    list_display = ('title','title_ae','title_he','title_ch','title_ur','title_ru','title_gr','title_sp')
    search_fields = ('title','title_ae',)
    
class skillAdmin(admin.ModelAdmin):  
    list_display = ('title',)
    search_fields = ('title',)

class settingAdmin(admin.ModelAdmin):  
    list_display = ('field','short_description')
    search_fields = ('title',)

class emailAdmin(admin.ModelAdmin):  
    list_display = ('subject','short_description')
    search_fields = ('subject',)

class jobpostAdmin(admin.ModelAdmin):  
    list_display = ('user_id','title','short_description')
    search_fields = ('subject','user_id')

class contactAdmin(admin.ModelAdmin):  
    list_display = ('fullname','email','message')
    search_fields = ('fullname','email')


admin.site.register(models.Category,categoryAdmin)
admin.site.register(models.NewSkills,skillAdmin)
admin.site.register(models.Users,userAdmin)
admin.site.register(models.Settings,settingAdmin)
admin.site.register(models.Emails,emailAdmin)
admin.site.register(models.ManagePosts,jobpostAdmin)
admin.site.register(models.UserContact,contactAdmin)



# Register your models here.
