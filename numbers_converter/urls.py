from django.urls import path

from numbers_converter.views import ConverterHomeView,ConverterFinishedView

urlpatterns = [
    path('', ConverterHomeView.as_view(), name='converter_home'),
    path('wynik/', ConverterFinishedView.as_view(), name='converter_finished'),
]
