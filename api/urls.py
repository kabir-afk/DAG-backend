from django.urls import path
from .views import ReadRoot ,ParsePipelineView

urlpatterns = [
    path('', ReadRoot.as_view()),
    path('pipelines/parse', ParsePipelineView.as_view()),
]