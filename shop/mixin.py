from .models import Category


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = Category.objects.all()
        return context