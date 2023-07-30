from django.db import models
from django.urls import reverse
# Create your models here.
# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="media/", default='C:/Users/dmaso/OneDrive/Desktop/R_School_Leaders/resilient_school_leaders/static/media/card-1.jpg')

    def get_absolute_url(self):
        template_mapping = {
            'Community Networking': 'community_networking.html',
            'Diversity and Inclusion': 'diversity_inclusion.html',
            'Leadership Development': 'leadership_development.html',
            'Professional Development': 'professional_development.html',
            'Team Building': 'team_building.html',
            'Wellbeing and Resilience': 'wellbeing_resilience.html',
        }
        
        template_name = template_mapping.get(self.category_name, 'default_template.html')
        return reverse('template_view', kwargs={'template_name': template_name})

    def resource_count(self):
        """
        Method that returns the count of resources for that category.
        """
        return Resource.objects.filter(category=self).count()

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = "Categories"


# Resource Model
class Resource(models.Model):
    ''' 
    This model represents a resource available on the website, such as an embedded video or external article. It could include fields such as:

        - Title (string)
        - Type (string; options could include "video", "article", etc.)
        - URL (string)
        - Description (text)
        - Date published (date)
        - Tags (many-to-many relationship with a Tag model; see below)
    '''
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/', default='C:/Users/dmaso/OneDrive/Desktop/R_School_Leaders/resilient_school_leaders/static/media/card-1.jpg')
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_published = models.DateField()
    # tags = models.CharField(max_length=250)

    def __str__(self):
        return self.title