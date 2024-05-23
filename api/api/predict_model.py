from django.urls import path
from .controllers import predict_model
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = {
    path('', predict_model, name="predict-model")
}

urlpatterns = format_suffix_patterns(urlpatterns)