from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


# detached views
from core.views import RegisterationView

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth 
    path("signup/", RegisterationView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),

    path("", include("campaigns.urls", namespace="campaigns")),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
