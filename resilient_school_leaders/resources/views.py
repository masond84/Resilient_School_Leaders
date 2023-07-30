from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Resource
from django.http import HttpResponse, JsonResponse

# Create your views here.
def resource_index(request):
    category = Category.objects.all()
    resource = Resource.objects.all()
    context = {
        'category': category,
        'resource': resource,
    }
    return render(request, 'resources/resources.html', context)

def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    return render(request, 'resources/resource_detail.html', {'resource': resource})

def category_resources(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    resources = Resource.objects.filter(category=category)
    context = {
        'category': category,
        'resources': resources
    }
    html = render(request, 'category_resources.html', context).content
    return JsonResponse({'html': html.decode('utf-8')})

#### ALL RESOURCES ####
def all_resources(request):
    category = Category.objects.all()
    resource = Resource.objects.all()
    context = {
        'category': category,
        'resource': resource,
    }
    return render(request, 'resources/resources_all.html', context)

#### RESOURCE CATEGORY PAGES ####
def leadership_development(request):
    category = get_object_or_404(Category, category_name="Leadership Development")
    resources = Resource.objects.filter(category=category)
    return render(request, 'resources/leadership_development.html', {'category': category, 'resources':resources})
def professional_development(request):
    category = get_object_or_404(Category, category_name="Professional Development")
    resources = Resource.objects.filter(category=category)
    return render(request, "resources/professional_development.html", {'category':category, 'resources':resources})
def wellbeing_resilience(request):
    category = get_object_or_404(Category, category_name="Wellbeing & Resilience")
    resources = Resource.objects.filter(category=category)
    return render(request, "resources/wellbeing_resilience.html", {'category':category, 'resources':resources})
def team_building(request):
    category = get_object_or_404(Category, category_name="Team Building & Collaboration")
    resources = Resource.objects.filter(category=category)
    return render(request, "resources/team_building.html", {'category':category, 'resources':resources})
def community_networking(request):
    category = get_object_or_404(Category, category_name="Community & Networking")
    resources = Resource.objects.filter(category=category)
    return render(request, "resources/community_networking.html", {'category':category, 'resources':resources})
def diversity_inclusion(request):
    category = get_object_or_404(Category, category_name="Diversity, Equity, & Inclusion")
    resources = Resource.objects.filter(category=category)
    return render(request, "resources/diversity_inclusion.html", {'category':category, 'resources':resources})
### MAYBE DELETE ###
def category_detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        # Handle the case where the category does not exist (e.g., show a 404 page)
        return redirect('resource_index')  # Redirect to the resource index page or another appropriate page

    category_url = category.get_absolute_url()
    return redirect(category_url)