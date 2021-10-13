from django.urls import include, path, re_path
from swagger.rest_framework_swagger.views import get_swagger_view

from apps.api import views

app_name = 'api'

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('', schema_view, name='api'),
    path('range-measure/<str:pair>/<str:mms>/', views.RangeMeasureView.as_view(), name='range-measure-mms'),
    path('range-measure/<str:pair>/', views.RangeMeasureView.as_view(), name='range-measure'),
]
