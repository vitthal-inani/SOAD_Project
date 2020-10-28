from django.urls import path, include
from Tourism import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.homepage, name="home"),
    path('register/', views.registration_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('email-verify/', views.verify_email, name="email-verify"),
    path('api/', include('Tourism.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)