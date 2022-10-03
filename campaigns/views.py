from django.shortcuts import render, reverse, get_object_or_404
from django.views import View

from . import CampaignStatus
from .models import Campaign
from .forms import SignForm, CampaignForm

class IndexView(View):

	def get(self, request, *args, **kwargs):
		campaigns = Campaign.objects.filter(
			is_confirmed=True
		) # only those confirmed by admin
		ongoing_objects = campaigns.filter(status=CampaignStatus.RUNNING)
		succeeded_objects = campaigns.filter(status=CampaignStatus.SUCCESSFUL)
		failed_objects = campaigns.filter(status=CampaignStatus.FAILDED)
		
		context = {
			"ongoing_objects": ongoing_objects,
			"succeeded_objects": succeeded_objects,
			"failed_objects": failed_objects,
		}
		return render(request, "index.html", context)

	# def post(self, request, *args, **kwargs):
	# 	pass 

class CampaignDetailView(View):

	def get(self, request, slug, *args, **kwargs):
		campaign = get_object_or_404(Campaign, slug=slug)
		return render(
			request,
			"campaigns/detail.html",
			context={"object": campaign},
		)

	# def post(self, request, *args, **kwargs):
	# 	pass


class CampaignCreateView(View):

	def get(self, request, *args, **kwargs):
		form = CampaignForm()
		context = {
			"form": form
		}
		return render(request, "campaigns/create.html", context)

	def post(self, request, *args, **kwargs):
		form = CampaignForm(request.POST)
		if form.is_valid():
			sign, created = form.save(form.validated_data)
			if created:
				messages.success(request, "Successfully signed the campaign")
			else:
				messages.info(request, "You have already signed this campaign")
			return redirect(reverse(
						"campaigns:create", args=(request.POST.get("slug"))
					))
		else:
			messages.warning(request, form.erros.json())
			return redirect("campaigns:create")


# #-----------------------------------
# #			API Views
# #-----------------------------------
# from django.http import JsonResponse