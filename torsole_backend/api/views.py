from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .serializers import GramPanchayatInfoSerializer, SlideShowSerializer, AboutVillageSerializer, MissionSerializer, MissionObjectivesSerializer, ImportantLinksSerializer, GovernmentGRSerializer, DepartmentSerializer, GramPanchayatDocumentsSerializer, PhotoGallerySerializer
from .models import GramPanchayatInfo, SlideShow, AboutVillage, Mission, MissionObjectives, ImportantLinks, GovernmentGR, Department, GramPanchayatDocuments, PhotoGallery
from .forms import GramPanchayatInfoForm, SlideShowForm, AboutVillageForm, MissionForm, MissionObjectivesForm, ImportantLinksForm, DepartmentForm, GovernmentGRForm, GramPanchayatDocumentsForm, PhotoGalleryForm

class GramPanchayatInfoViewSet(viewsets.ModelViewSet):
    serializer_class = GramPanchayatInfoSerializer
    queryset = GramPanchayatInfo.objects.all()

class SlideShowViewSet(viewsets.ModelViewSet):
    serializer_class = SlideShowSerializer
    queryset = SlideShow.objects.all()

class AboutVillageViewset(viewsets.ModelViewSet):
    serializer_class = AboutVillageSerializer
    queryset = AboutVillage.objects.all()

class MissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()

class MissionObjectivesViewSet(viewsets.ModelViewSet):
    serializer_class = MissionObjectivesSerializer
    queryset = MissionObjectives.objects.all()

class ImportantLinksViewset(viewsets.ModelViewSet):
    serializer_class = ImportantLinksSerializer
    queryset = ImportantLinks.objects.all()

class GovernmentGRViewset(viewsets.ModelViewSet):
    serializer_class = GovernmentGRSerializer
    queryset = GovernmentGR.objects.all()

class DepartmentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class GramPanchayatDocumentsViewset(viewsets.ModelViewSet):
    serializer_class = GramPanchayatDocumentsSerializer
    queryset = GramPanchayatDocuments.objects.all()

class PhotoGalleryViewset(viewsets.ModelViewSet):
    serializer_class = PhotoGallerySerializer
    queryset = PhotoGallery.objects.all()





def admin_login(request):
    image = SlideShow.objects.get(id = 1)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'auth/admin_login.html', {'img': image.image})
    return render(request, 'auth/admin_login.html', {'img': image.image})


@login_required(login_url='/admin/login/')
def Dashboard(request):
    user = request.user.username
    # Get counts for overview cards
    slideshow_count = SlideShow.objects.count()
    about_village_count = AboutVillage.objects.count()
    important_links_count = ImportantLinks.objects.count()
    mission_count = Mission.objects.count()
    mission_objectives_count = MissionObjectives.objects.count()
    department_count = Department.objects.count()
    government_gr_count = GovernmentGR.objects.count()
    gp_documents_count = GramPanchayatDocuments.objects.count()
    photo_gallery_count = PhotoGallery.objects.count()

    # Get latest items from each model
    latest_slideshow = SlideShow.objects.order_by('-updated_at').first()
    latest_about_village = AboutVillage.objects.order_by('-updated_at').first()
    latest_important_link = ImportantLinks.objects.order_by('-updated_at').first()
    latest_mission = Mission.objects.order_by('-id').first()  # No date field, use -id
    latest_mission_objective = MissionObjectives.objects.order_by('-id').first()  # No date field, use -id
    latest_department = Department.objects.order_by('-id').first()  # No date field, use -id
    latest_government_gr = GovernmentGR.objects.order_by('-upload_date').first()
    latest_gp_document = GramPanchayatDocuments.objects.order_by('-upload_date').first()
    latest_photo_gallery = PhotoGallery.objects.order_by('-upload_date').first()

    context = {
        'user': user,
        'slideshow_count': slideshow_count,
        'about_village_count': about_village_count,
        'important_links_count': important_links_count,
        'mission_count': mission_count,
        'mission_objectives_count': mission_objectives_count,
        'department_count': department_count,
        'government_gr_count': government_gr_count,
        'gp_documents_count': gp_documents_count,
        'photo_gallery_count': photo_gallery_count,
        'latest_slideshow': latest_slideshow,
        'latest_about_village': latest_about_village,
        'latest_important_link': latest_important_link,
        'latest_mission': latest_mission,
        'latest_mission_objective': latest_mission_objective,
        'latest_department': latest_department,
        'latest_government_gr': latest_government_gr,
        'latest_gp_document': latest_gp_document,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='/admin/login/')
def AboutGp(request):
    gp_infos = GramPanchayatInfo.objects.all()
    return render(request, 'dashboard/about_gp.html', {'gp_infos': gp_infos})

@login_required(login_url='/admin/login/')
def gp_info_create(request):
    # Check if a record already exists
    existing_info = GramPanchayatInfo.objects.first()
    if existing_info:
        return redirect('gp-info-update', pk=existing_info.pk)

    if request.method == 'POST':
        form = GramPanchayatInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'ग्रामपंचायत माहिती यशस्वीरित्या जोडली गेली!')
            return redirect('about-gp')
    else:
        form = GramPanchayatInfoForm()
    return render(request, 'dashboard/gp_info_form.html', {'form': form, 'title': 'ग्रामपंचायत माहिती जोडा'})

@login_required(login_url='/admin/login/')
def gp_info_update(request, pk):
    gp_info = get_object_or_404(GramPanchayatInfo, pk=pk)
    if request.method == 'POST':
        form = GramPanchayatInfoForm(request.POST, request.FILES, instance=gp_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'ग्रामपंचायत माहिती यशस्वीरित्या अपडेट केली गेली!')
            return redirect('about-gp')
    else:
        form = GramPanchayatInfoForm(instance=gp_info)
    return render(request, 'dashboard/gp_info_form.html', {'form': form, 'title': 'ग्रामपंचायत माहिती संपादित करा'})

@login_required(login_url='/admin/login/')
def gp_info_delete(request, pk):
    gp_info = get_object_or_404(GramPanchayatInfo, pk=pk)
    if request.method == 'POST':
        gp_info.delete()
        messages.success(request, 'ग्रामपंचायत माहिती यशस्वीरित्या हटवली गेली!')
        return redirect('about-gp')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/admin/login/')
def slideshow_list(request):
    slideshows = SlideShow.objects.all()
    return render(request, 'dashboard/slideshow_list.html', {'slideshows': slideshows})

@login_required(login_url='/admin/login/')
def slideshow_create(request):
    if request.method == 'POST':
        form = SlideShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'स्लाईड शो यशस्वीरित्या जोडला गेला!')
            return redirect('slideshow-list')
    else:
        form = SlideShowForm()
    return render(request, 'dashboard/slideshow_form.html', {'form': form, 'title': 'स्लाईड शो जोडा'})

@login_required(login_url='/admin/login/')
def slideshow_update(request, pk):
    slideshow = get_object_or_404(SlideShow, pk=pk)
    if request.method == 'POST':
        form = SlideShowForm(request.POST, request.FILES, instance=slideshow)
        if form.is_valid():
            form.save()
            messages.success(request, 'स्लाईड शो यशस्वीरित्या अपडेट केला गेला!')
            return redirect('slideshow-list')
    else:
        form = SlideShowForm(instance=slideshow)
    return render(request, 'dashboard/slideshow_form.html', {'form': form, 'title': 'स्लाईड शो संपादित करा'})

@login_required(login_url='/admin/login/')
def slideshow_delete(request, pk):
    slideshow = get_object_or_404(SlideShow, pk=pk)
    if request.method == 'POST':
        slideshow.delete()
        messages.success(request, 'स्लाईड शो यशस्वीरित्या हटवला गेला!')
        return redirect('slideshow-list')
    return render(request, 'dashboard/slideshow_delete.html', {'slideshow': slideshow})

@login_required(login_url='/admin/login/')
def about_village_list(request):
    about_villages = AboutVillage.objects.all()
    return render(request, 'dashboard/about_village_list.html', {'about_villages': about_villages})

@login_required(login_url='/admin/login/')
def about_village_create(request):
    # Check if a record already exists
    existing_info = AboutVillage.objects.first()
    if existing_info:
        return redirect('about-village-update', pk=existing_info.pk)

    if request.method == 'POST':
        form = AboutVillageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'गावाची माहिती यशस्वीरित्या जोडली गेली!')
            return redirect('about-village-list')
    else:
        form = AboutVillageForm()
    return render(request, 'dashboard/about_village_form.html', {'form': form, 'title': 'गावाची माहिती जोडा'})

@login_required(login_url='/admin/login/')
def about_village_update(request, pk):
    about_village = get_object_or_404(AboutVillage, pk=pk)
    if request.method == 'POST':
        form = AboutVillageForm(request.POST, instance=about_village)
        if form.is_valid():
            form.save()
            messages.success(request, 'गावाची माहिती यशस्वीरित्या अपडेट केली गेली!')
            return redirect('about-village-list')
    else:
        form = AboutVillageForm(instance=about_village)
    return render(request, 'dashboard/about_village_form.html', {'form': form, 'title': 'गावाची माहिती संपादित करा'})

@login_required(login_url='/admin/login/')
def about_village_delete(request, pk):
    about_village = get_object_or_404(AboutVillage, pk=pk)
    if request.method == 'POST':
        about_village.delete()
        messages.success(request, 'गावाची माहिती यशस्वीरित्या हटवली गेली!')
        return redirect('about-village-list')
    return render(request, 'dashboard/about_village_delete.html', {'about_village': about_village})

@login_required(login_url='/admin/login/')
def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'dashboard/mission_list.html', {'missions': missions})

@login_required(login_url='/admin/login/')
def mission_create(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'मिशन यशस्वीरित्या जोडले गेले!')
            return redirect('mission-list')
    else:
        form = MissionForm()
    return render(request, 'dashboard/mission_form.html', {'form': form, 'title': 'मिशन जोडा'})

@login_required(login_url='/admin/login/')
def mission_update(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            messages.success(request, 'मिशन यशस्वीरित्या अपडेट केले गेले!')
            return redirect('mission-list')
    else:
        form = MissionForm(instance=mission)
    return render(request, 'dashboard/mission_form.html', {'form': form, 'title': 'मिशन संपादित करा'})

@login_required(login_url='/admin/login/')
def mission_delete(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'POST':
        mission.delete()
        messages.success(request, 'मिशन यशस्वीरित्या हटवले गेले!')
        return redirect('mission-list')
    return render(request, 'dashboard/mission_delete.html', {'mission': mission})

@login_required(login_url='/admin/login/')
def mission_objectives_list(request):
    mission_objectives = MissionObjectives.objects.all()
    return render(request, 'dashboard/mission_objectives_list.html', {'mission_objectives': mission_objectives})

@login_required(login_url='/admin/login/')
def mission_objectives_create(request):
    if request.method == 'POST':
        form = MissionObjectivesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'मिशन उद्दिष्टे यशस्वीरित्या जोडली गेली!')
            return redirect('mission-objectives-list')
    else:
        form = MissionObjectivesForm()
    return render(request, 'dashboard/mission_objectives_form.html', {'form': form, 'title': 'मिशन उद्दिष्टे जोडा'})

@login_required(login_url='/admin/login/')
def mission_objectives_update(request, pk):
    mission_objective = get_object_or_404(MissionObjectives, pk=pk)
    if request.method == 'POST':
        form = MissionObjectivesForm(request.POST, instance=mission_objective)
        if form.is_valid():
            form.save()
            messages.success(request, 'मिशन उद्दिष्टे यशस्वीरित्या अपडेट केली गेली!')
            return redirect('mission-objectives-list')
    else:
        form = MissionObjectivesForm(instance=mission_objective)
    return render(request, 'dashboard/mission_objectives_form.html', {'form': form, 'title': 'मिशन उद्दिष्टे संपादित करा'})

@login_required(login_url='/admin/login/')
def mission_objectives_delete(request, pk):
    mission_objective = get_object_or_404(MissionObjectives, pk=pk)
    if request.method == 'POST':
        mission_objective.delete()
        messages.success(request, 'मिशन उद्दिष्टे यशस्वीरित्या हटवली गेली!')
        return redirect('mission-objectives-list')
    return render(request, 'dashboard/mission_objectives_delete.html', {'mission_objective': mission_objective})

@login_required(login_url='/admin/login/')
def important_links_list(request):
    important_links = ImportantLinks.objects.all()
    return render(request, 'dashboard/important_links_list.html', {'important_links': important_links})

@login_required(login_url='/admin/login/')
def important_links_create(request):
    if request.method == 'POST':
        form = ImportantLinksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'महत्वाच्या लिंक यशस्वीरित्या जोडल्या गेल्या!')
            return redirect('important-links-list')
    else:
        form = ImportantLinksForm()
    return render(request, 'dashboard/important_links_form.html', {'form': form, 'title': 'महत्वाच्या लिंक जोडा'})

@login_required(login_url='/admin/login/')
def important_links_update(request, pk):
    important_link = get_object_or_404(ImportantLinks, pk=pk)
    if request.method == 'POST':
        form = ImportantLinksForm(request.POST, request.FILES, instance=important_link)
        if form.is_valid():
            form.save()
            messages.success(request, 'महत्वाच्या लिंक यशस्वीरित्या अपडेट केल्या गेल्या!')
            return redirect('important-links-list')
    else:
        form = ImportantLinksForm(instance=important_link)
    return render(request, 'dashboard/important_links_form.html', {'form': form, 'title': 'महत्वाच्या लिंक संपादित करा'})

@login_required(login_url='/admin/login/')
def important_links_delete(request, pk):
    important_link = get_object_or_404(ImportantLinks, pk=pk)
    if request.method == 'POST':
        important_link.delete()
        messages.success(request, 'महत्वाच्या लिंक यशस्वीरित्या हटवल्या गेल्या!')
        return redirect('important-links-list')
    return render(request, 'dashboard/important_links_delete.html', {'important_link': important_link})

@login_required(login_url='/admin/login/')
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'dashboard/department_list.html', {'departments': departments})

@login_required(login_url='/admin/login/')
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'विभाग यशस्वीरित्या जोडला गेला!')
            return redirect('department-list')
    else:
        form = DepartmentForm()
    return render(request, 'dashboard/department_form.html', {'form': form, 'title': 'विभाग जोडा'})

@login_required(login_url='/admin/login/')
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'विभाग यशस्वीरित्या अपडेट केला गेला!')
            return redirect('department-list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'dashboard/department_form.html', {'form': form, 'title': 'विभाग संपादित करा'})

@login_required(login_url='/admin/login/')
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'विभाग यशस्वीरित्या हटवला गेला!')
        return redirect('department-list')
    return render(request, 'dashboard/department_delete.html', {'department': department})

@login_required(login_url='/admin/login/')
def government_gr_list(request):
    government_grs = GovernmentGR.objects.all()
    return render(request, 'dashboard/government_gr_list.html', {'government_grs': government_grs})

@login_required(login_url='/admin/login/')
def government_gr_create(request):
    if request.method == 'POST':
        form = GovernmentGRForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'शासन निर्णय यशस्वीरित्या जोडला गेला!')
            return redirect('government-gr-list')
    else:
        form = GovernmentGRForm()
    return render(request, 'dashboard/government_gr_form.html', {'form': form, 'title': 'शासन निर्णय जोडा'})

@login_required(login_url='/admin/login/')
def government_gr_update(request, pk):
    government_gr = get_object_or_404(GovernmentGR, pk=pk)
    if request.method == 'POST':
        form = GovernmentGRForm(request.POST, request.FILES, instance=government_gr)
        if form.is_valid():
            form.save()
            messages.success(request, 'शासन निर्णय यशस्वीरित्या अपडेट केला गेला!')
            return redirect('government-gr-list')
    else:
        form = GovernmentGRForm(instance=government_gr)
    return render(request, 'dashboard/government_gr_form.html', {'form': form, 'title': 'शासन निर्णय संपादित करा'})

@login_required(login_url='/admin/login/')
def government_gr_delete(request, pk):
    government_gr = get_object_or_404(GovernmentGR, pk=pk)
    if request.method == 'POST':
        government_gr.delete()
        messages.success(request, 'शासन निर्णय यशस्वीरित्या हटवला गेला!')
        return redirect('government-gr-list')
    return render(request, 'dashboard/government_gr_delete.html', {'government_gr': government_gr})

@login_required(login_url='/admin/login/')
def gp_documents_list(request):
    gp_documents = GramPanchayatDocuments.objects.all()
    return render(request, 'dashboard/gp_documents_list.html', {'gp_documents': gp_documents})

@login_required(login_url='/admin/login/')
def gp_documents_create(request):
    if request.method == 'POST':
        form = GramPanchayatDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'ग्रामपंचायत दस्तऐवज यशस्वीरित्या जोडला गेला!')
            return redirect('gp-documents-list')
    else:
        form = GramPanchayatDocumentsForm()
    return render(request, 'dashboard/gp_documents_form.html', {'form': form, 'title': 'ग्रामपंचायत दस्तऐवज जोडा'})

@login_required(login_url='/admin/login/')
def gp_documents_update(request, pk):
    gp_document = get_object_or_404(GramPanchayatDocuments, pk=pk)
    if request.method == 'POST':
        form = GramPanchayatDocumentsForm(request.POST, request.FILES, instance=gp_document)
        if form.is_valid():
            form.save()
            messages.success(request, 'ग्रामपंचायत दस्तऐवज यशस्वीरित्या अपडेट केला गेला!')
            return redirect('gp-documents-list')
    else:
        form = GramPanchayatDocumentsForm(instance=gp_document)
    return render(request, 'dashboard/gp_documents_form.html', {'form': form, 'title': 'ग्रामपंचायत दस्तऐवज संपादित करा'})

@login_required(login_url='/admin/login/')
def gp_documents_delete(request, pk):
    gp_document = get_object_or_404(GramPanchayatDocuments, pk=pk)
    if request.method == 'POST':
        gp_document.delete()
        messages.success(request, 'ग्रामपंचायत दस्तऐवज यशस्वीरित्या हटवला गेला!')
        return redirect('gp-documents-list')
    return render(request, 'dashboard/gp_documents_delete.html', {'gp_document': gp_document})

@login_required(login_url='/admin/login/')
def photo_gallery_list(request):
    photo_galleries = PhotoGallery.objects.all()
    return render(request, 'dashboard/photo_gallery_list.html', {'photo_galleries': photo_galleries})

@login_required(login_url='/admin/login/')
def photo_gallery_create(request):
    if request.method == 'POST':
        form = PhotoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'फोटो गॅलरी यशस्वीरित्या जोडली गेली!')
            return redirect('photo-gallery-list')
    else:
        form = PhotoGalleryForm()
    return render(request, 'dashboard/photo_gallery_form.html', {'form': form, 'title': 'फोटो गॅलरी जोडा'})

@login_required(login_url='/admin/login/')
def photo_gallery_update(request, pk):
    photo_gallery = get_object_or_404(PhotoGallery, pk=pk)
    if request.method == 'POST':
        form = PhotoGalleryForm(request.POST, request.FILES, instance=photo_gallery)
        if form.is_valid():
            form.save()
            messages.success(request, 'फोटो गॅलरी यशस्वीरित्या अपडेट केली गेली!')
            return redirect('photo-gallery-list')
    else:
        form = PhotoGalleryForm(instance=photo_gallery)
    return render(request, 'dashboard/photo_gallery_form.html', {'form': form, 'title': 'फोटो गॅलरी संपादित करा'})

@login_required(login_url='/admin/login/')
def photo_gallery_delete(request, pk):
    photo_gallery = get_object_or_404(PhotoGallery, pk=pk)
    if request.method == 'POST':
        photo_gallery.delete()
        messages.success(request, 'फोटो गॅलरी यशस्वीरित्या हटवली गेली!')
        return redirect('photo-gallery-list')
    return render(request, 'dashboard/photo_gallery_delete.html', {'photo_gallery': photo_gallery})
