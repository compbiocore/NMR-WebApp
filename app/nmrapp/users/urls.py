from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.Insertrecord),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('analysis/', views.analysis, name='analysis'),
    path('retrieve/', views.serve_file, name='retrieve'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]

# Only during development - for production will need to change
if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

