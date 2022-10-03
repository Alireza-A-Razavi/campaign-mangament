from django.urls import path 

from . import views

app_name = "campaigns"

urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path("<str:slug>/", views.CampaignDetailView.as_view(), name="detail"),
]