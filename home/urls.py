from django.urls import path
from .views import home, about, teachers


urlpatterns = [
    path('', home, name='home' ),
    path('about', about, name='about' ),
    path('teachers', teachers, name='teachers' ),
]
