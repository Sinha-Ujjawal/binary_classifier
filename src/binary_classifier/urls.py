"""binary_classifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.schemas import get_schema_view
from binary_classifier_app import views

schema_view = get_schema_view(
    title="Binary Classifier", description="Served APIs", version="1.0.0"
)

urlpatterns = [
    path("", schema_view),
    path("admin/", admin.site.urls),
    path("classifier/train", views.Train.as_view()),
    path("classifier/test", views.Test.as_view()),
    path(
        "classifier/decisionBoundary/<int:model_id>", views.DecisionBoundary.as_view()
    ),
    path("classifier/models", views.ModelIds.as_view()),
    path("classifier/deleteModel/<int:model_id>", views.DeleteModel.as_view()),
]
