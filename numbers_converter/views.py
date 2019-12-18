from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from numbers_converter.forms import ConverterForm
from numbers_converter.services import ConverterService


class ConverterHomeView(FormView):
    template_name = 'numbers_converter/index.html'
    form_class = ConverterForm
    success_url = reverse_lazy('converter_finished')

    def form_valid(self, form):
        number = form.cleaned_data['number']
        converted_number = ConverterService.number_to_text(number)
        self.request.session['converted_number'] = converted_number
        return super().form_valid(form)


class ConverterFinishedView(TemplateView):
    template_name = 'numbers_converter/finished.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        if 'converted_number' in self.request.session:
            context['converted_number'] = self.request.session['converted_number']
            del self.request.session['converted_number']

        return context
