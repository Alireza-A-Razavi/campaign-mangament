from django import forms 
from django.core.exceptions import ObjectDoesNotExist
from django_quill.forms import QuillFormField

from .models import Sign, Campaign

class CampaignForm(forms.ModelForm):
	description = QuillFormField()

	class Meta:
		model = Campaign
		fields = (
			"creator",
			"name",
			"slug",
			"image",
			"description",
			"status",
			"is_confirmed",
		)


class SignForm(forms.Form):
	owner = forms.IntegerField()
	slug = forms.CharField()

	def save(self, validated_data, *args, **kwargs):
		try:
			user = User.objects.get(
				pk=validated_data.get("user")
			)
			campaign = Campaign.objects.get(
				slug=validated_data.get("slug")
			)
		except ObjectDoesNotExist:
			raise forms.ValidationError("There is no user with provided id or campaign with slug")
		except Exception as E:
			print(E)
			raise Exception
		sign, created = Sign.objects.get_or_create(
			user=user,
			campaign=campaign,
		)
		return sign, created