from django.contrib import admin
from .models import GramPanchayatInfo, SlideShow, AboutVillage, MissionObjectives, Mission, ImportantLinks, Department, GovernmentGR

class MissionInline(admin.TabularInline):
    model = MissionObjectives.missions.through
    extra = 1

class MissionObjectivesAdmin(admin.ModelAdmin):
    inlines = [MissionInline]
    exclude = ('missions',)

admin.site.register(GramPanchayatInfo)
admin.site.register(SlideShow)
admin.site.register(AboutVillage)
admin.site.register(ImportantLinks)
admin.site.register(Mission)
admin.site.register(MissionObjectives, MissionObjectivesAdmin)
admin.site.register(Department)
admin.site.register(GovernmentGR)
