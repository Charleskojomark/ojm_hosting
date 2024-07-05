from .models import ServiceCategory,Service

def global_context(request):
    categories = ServiceCategory.objects.all()[:6]
    
    return {
        'categories': categories,
    }