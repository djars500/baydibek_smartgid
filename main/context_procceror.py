from .models import MediaCategory, Category

def load_categories(request):
    media_cat = MediaCategory.objects.all()
    cat = Category.objects.all()

    return {
        'media_cat':media_cat,
        'cat': cat
    }