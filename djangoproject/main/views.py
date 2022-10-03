from django.views.generic.base import TemplateView


class MyTemplateView(TemplateView):
    template_name = "main/cards.html"

    def get_context_data(self, **kwargs):
        return super(MyTemplateView, self).get_context_data(**kwargs)
