from django.shortcuts import render, redirect,get_object_or_404
from .forms import ClientForm 
from member.models import Client
from blogs.models import Blog
from django.http import JsonResponse
# Create your views here.
def home(request):    
    context = {
        'clients': Client.objects.all(),
        'blogs': Blog.objects.all(),
        
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def course(request, courseid,username):
    context = {'course_id': courseid,'user':username}
    return render(request, 'course.html', context)

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_client')  # or redirect to some success page
    else:
        form = ClientForm()

    return render(request, 'add_client.html', {'form': form})

def view_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'view_client.html', {'client': client})

def viewclients(request):
    clients = Client.objects.all()
    return render(request, 'viewclients.html', {'clients': clients})

def api_client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    # Get image URLs
    images = [img.image.url for img in client.project_images.all()]

    data = {
        'id': client.id,
        'name': client.name,
        'client_code': client.client_code,
        'contact': client.contact,
        'address': client.address,
        'description': client.description,
        'status': client.project_status,
        'url': client.url_link,
        'project_images': request.build_absolute_uri()[:-1] + images[0] if images else [],
    }

    return JsonResponse(data)