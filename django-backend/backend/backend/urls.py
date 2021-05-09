from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from patient import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientView, 'patient')
router.register(r'diagnosis', views.DiagnosisView, 'diagnosis')
router.register(r'drugs', views.DrugsView, 'drugs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
