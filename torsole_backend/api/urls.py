from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import GramPanchayatInfoViewSet, SlideShowViewSet, AboutVillageViewset, MissionViewSet, MissionObjectivesViewSet, ImportantLinksViewset, GovernmentGRViewset, DepartmentViewset, GramPanchayatDocumentsViewset, PhotoGalleryViewset, GrampanchayatBodiesViewSet, MaharastraOfficersViewSet, TorsoleVillagePopulationViewSet
from . import views

router = routers.DefaultRouter()
router.register('gpinfo', GramPanchayatInfoViewSet)
router.register('grampanchayat-bodies', GrampanchayatBodiesViewSet)
router.register('maharastra-officers', MaharastraOfficersViewSet)
router.register('torsole-village-population', TorsoleVillagePopulationViewSet)
router.register('slideshow', SlideShowViewSet)
router.register('about-village', AboutVillageViewset)
router.register('missions', MissionViewSet)
router.register('mission-objectives', MissionObjectivesViewSet)
router.register('important-links', ImportantLinksViewset)
router.register('goverment-grs', GovernmentGRViewset)
router.register('gr-departments', DepartmentViewset)
router.register('gp-documents', GramPanchayatDocumentsViewset)
router.register('photo-gallery', PhotoGalleryViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/login', views.admin_login, name='login'),
    path('dashboard', views.Dashboard, name="dashboard"),
    path('dashboard/about-gp', views.AboutGp, name="about-gp"),
    path('gp-info/create/', views.gp_info_create, name='gp-info-create'),
    path('gp-info/update/<int:pk>/', views.gp_info_update, name='gp-info-update'),
    path('gp-info/delete/<int:pk>/', views.gp_info_delete, name='gp-info-delete'),
    path('dashboard/slideshow/', views.slideshow_list, name='slideshow-list'),
    path('dashboard/slideshow/create/', views.slideshow_create, name='slideshow-create'),
    path('dashboard/slideshow/update/<int:pk>/', views.slideshow_update, name='slideshow-update'),
    path('dashboard/slideshow/delete/<int:pk>/', views.slideshow_delete, name='slideshow-delete'),
    path('dashboard/about-village/', views.about_village_list, name='about-village-list'),
    path('dashboard/about-village/create/', views.about_village_create, name='about-village-create'),
    path('dashboard/about-village/update/<int:pk>/', views.about_village_update, name='about-village-update'),
    path('dashboard/about-village/delete/<int:pk>/', views.about_village_delete, name='about-village-delete'),
    path('dashboard/mission/', views.mission_list, name='mission-list'),
    path('dashboard/mission/create/', views.mission_create, name='mission-create'),
    path('dashboard/mission/update/<int:pk>/', views.mission_update, name='mission-update'),
    path('dashboard/mission/delete/<int:pk>/', views.mission_delete, name='mission-delete'),
    path('dashboard/mission-objectives/', views.mission_objectives_list, name='mission-objectives-list'),
    path('dashboard/mission-objectives/create/', views.mission_objectives_create, name='mission-objectives-create'),
    path('dashboard/mission-objectives/update/<int:pk>/', views.mission_objectives_update, name='mission-objectives-update'),
    path('dashboard/mission-objectives/delete/<int:pk>/', views.mission_objectives_delete, name='mission-objectives-delete'),
    path('dashboard/important-links/', views.important_links_list, name='important-links-list'),
    path('dashboard/important-links/create/', views.important_links_create, name='important-links-create'),
    path('dashboard/important-links/update/<int:pk>/', views.important_links_update, name='important-links-update'),
    path('dashboard/important-links/delete/<int:pk>/', views.important_links_delete, name='important-links-delete'),
    path('dashboard/department/', views.department_list, name='department-list'),
    path('dashboard/department/create/', views.department_create, name='department-create'),
    path('dashboard/department/update/<int:pk>/', views.department_update, name='department-update'),
    path('dashboard/department/delete/<int:pk>/', views.department_delete, name='department-delete'),
    path('dashboard/government-gr/', views.government_gr_list, name='government-gr-list'),
    path('dashboard/government-gr/create/', views.government_gr_create, name='government-gr-create'),
    path('dashboard/government-gr/update/<int:pk>/', views.government_gr_update, name='government-gr-update'),
    path('dashboard/government-gr/delete/<int:pk>/', views.government_gr_delete, name='government-gr-delete'),
    path('dashboard/gp-documents/', views.gp_documents_list, name='gp-documents-list'),
    path('dashboard/gp-documents/create/', views.gp_documents_create, name='gp-documents-create'),
    path('dashboard/gp-documents/update/<int:pk>/', views.gp_documents_update, name='gp-documents-update'),
    path('dashboard/gp-documents/delete/<int:pk>/', views.gp_documents_delete, name='gp-documents-delete'),
    path('dashboard/photo-gallery/', views.photo_gallery_list, name='photo-gallery-list'),
    path('dashboard/photo-gallery/create/', views.photo_gallery_create, name='photo-gallery-create'),
    path('dashboard/photo-gallery/update/<int:pk>/', views.photo_gallery_update, name='photo-gallery-update'),
    path('dashboard/photo-gallery/delete/<int:pk>/', views.photo_gallery_delete, name='photo-gallery-delete'),
    path('dashboard/grampanchayat-bodies/', views.grampanchayat_bodies_list, name='grampanchayat-bodies-list'),
    path('dashboard/grampanchayat-bodies/create/', views.grampanchayat_bodies_create, name='grampanchayat-bodies-create'),
    path('dashboard/grampanchayat-bodies/update/<int:pk>/', views.grampanchayat_bodies_update, name='grampanchayat-bodies-update'),
    path('dashboard/grampanchayat-bodies/delete/<int:pk>/', views.grampanchayat_bodies_delete, name='grampanchayat-bodies-delete'),
    path('dashboard/maharastra-officers/', views.maharastra_officers_list, name='maharastra-officers-list'),
    path('dashboard/maharastra-officers/create/', views.maharastra_officers_create, name='maharastra-officers-create'),
    path('dashboard/maharastra-officers/update/<int:pk>/', views.maharastra_officers_update, name='maharastra-officers-update'),
    path('dashboard/maharastra-officers/delete/<int:pk>/', views.maharastra_officers_delete, name='maharastra-officers-delete'),
    path('dashboard/torsole-village-population/', views.torsole_village_population_list, name='torsole-village-population-list'),
    path('dashboard/torsole-village-population/create/', views.torsole_village_population_create, name='torsole-village-population-create'),
    path('dashboard/torsole-village-population/update/<int:pk>/', views.torsole_village_population_update, name='torsole-village-population-update'),
    path('dashboard/torsole-village-population/delete/<int:pk>/', views.torsole_village_population_delete, name='torsole-village-population-delete'),
    path('logout', views.logout_view, name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)