from django.urls import path
from . import views

urlpatterns = [
    # resource landing page
    path("", views.resource_index, name="resource_index"),
    # takes a 'resource_id' resource detail page for specific resources
    path('<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    # takes user to a page with all of the resources
    path("all_resources/", views.all_resources, name="all_resources"),
    # category pages with individual resources
    path("leadership_development/", views.leadership_development, name="leadership_development"),
    path("professional_development/", views.professional_development, name="professional_development"),
    path("wellbeing_resilience/", views.wellbeing_resilience, name="wellbeing_resilience"),
    path("teambuilding_collabortion/", views.team_building, name="team_building"),
    path("community_networking/", views.community_networking, name="community_networking"),
    path("diversity_equity_inclusion/", views.diversity_inclusion, name="diversity_inclusion"),

]
