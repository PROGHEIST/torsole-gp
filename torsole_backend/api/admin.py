from django.contrib import admin
from .models import GramPanchayatInfo, SlideShow, AboutVillage, MissionObjectives, Mission, ImportantLinks, Department, GovernmentGR, GramPanchayatDocuments, PhotoGallery, GrampanchayatBodies, MaharastraOfficers, TorsoleVillagePopulation

class MissionInline(admin.TabularInline):
    model = MissionObjectives.missions.through
    extra = 1

class MissionObjectivesAdmin(admin.ModelAdmin):
    inlines = [MissionInline]
    exclude = ('missions',)

class TorsoleVillagePopulationAdmin(admin.ModelAdmin):
    list_display = ('from_year', 'to_year', 'vilage_name', 'family_count', 'population')
    list_filter = ('to_year',)

class GrampanchayatBodiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'updated_at')
    list_filter = ('position',)
    search_fields = ('name', 'position')

class MaharastraOfficersAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'updated_at')
    list_filter = ('position',)
    search_fields = ('name', 'position')

admin.site.register(GramPanchayatInfo)
admin.site.register(SlideShow)
admin.site.register(AboutVillage)
admin.site.register(ImportantLinks)
admin.site.register(Mission)
admin.site.register(MissionObjectives, MissionObjectivesAdmin)
admin.site.register(Department)
admin.site.register(GovernmentGR)
admin.site.register(GramPanchayatDocuments)
admin.site.register(PhotoGallery)
admin.site.register(GrampanchayatBodies, GrampanchayatBodiesAdmin)
admin.site.register(MaharastraOfficers, MaharastraOfficersAdmin)
admin.site.register(TorsoleVillagePopulation)