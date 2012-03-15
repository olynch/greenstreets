from django.forms import ModelForm, TextInput

from survey.models import School, Studentsurvey, Child, Schooldistrict, Employer, Street, Commutersurvey, Walkrideday, Sponsor, EmployerGSI
# from django.contrib import admin
from django.contrib.gis import admin


# default GeoAdmin overloads
admin.GeoModelAdmin.default_lon = -7915039
admin.GeoModelAdmin.default_lat = 5216500 #5220376  
admin.GeoModelAdmin.default_zoom = 12

class DistrictAdmin(admin.OSMGeoAdmin):
    prepopulated_fields = {'slug': ('distname',)}

class SchoolAdmin(admin.OSMGeoAdmin):
    fieldsets = [
        (None, 
            {'fields': ['name', 'slug', 'survey_active', 'districtid', 'survey_incentive']}),
        ('School Database Attributes', 
            {'fields': ['schid', 'address', 'town', 'state', 'zip', 'principal', 'phone', 'fax', 'grades', 'schl_type']}),
        ('Map',
            {'fields': ['geometry', ]}),
    ]    
    list_filter = ['survey_active']
    list_display = ('name', 'survey_count', 'town', 'grades', 'principal','phone',)
    search_fields = ['name', 'districtid__distname']
    ordering = ['districtid__distname']
    prepopulated_fields = {'slug': ('name',)}
    
    def survey_count(self, obj):
        return obj.survey_set.count()


class CommutersurveyAdminForm(ModelForm):
  class Meta:
    model = Commutersurvey
    widgets = {
        'employer': TextInput(),
    }

class CommutersurveyAdmin(admin.OSMGeoAdmin):
    form = CommutersurveyAdminForm


class SponsorAdminForm(ModelForm):
    class Meta:
        model = Sponsor
        widgets = {
            'employer': TextInput(),
        }

class SponsorAdmin(admin.ModelAdmin):
    form = CommutersurveyAdminForm
    
class StudentsurveyAdmin(admin.OSMGeoAdmin):
    list_display = ('pk','school')
    search_fields = ['school__name']

class ChildAdmin(admin.ModelAdmin):
    list_display = ('pk','survey')

class EmployerAdmin(admin.OSMGeoAdmin):
    search_fields = ['name', 'infousa_id']

class WalkridedayAdmin(admin.ModelAdmin):
    list_display = ['date', 'start_date', 'end_date']

class EmployerGSIAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display_links = ['id']
    list_display = ['id', 'name']
    list_editable = ['name']

admin.site.register(Schooldistrict, DistrictAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Studentsurvey, StudentsurveyAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Street, admin.OSMGeoAdmin)
admin.site.register(Commutersurvey, CommutersurveyAdmin)
admin.site.register(Walkrideday, WalkridedayAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(EmployerGSI, EmployerGSIAdmin)