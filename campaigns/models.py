from django.db import models
from django.contrib.auth import get_user_model

from django_quill.fields import QuillField

from . import CampaignStatus
from core.models import CreationModificationDateAbstractModel
from core.utils import unique_slug_generator

User = get_user_model()

class Campaign(CreationModificationDateAbstractModel):
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	slug = models.SlugField(blank=True, null=True)
	image = models.ImageField(
		upload_to="campaings/", 
		default="/media/campaings/dummy.png",
	)
	description = QuillField()
	status = models.CharField(max_length=16, choices=CampaignStatus.CHOICES)
	is_confirmed = models.BooleanField(default=False) # admin confirmes the campaigns

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = unique_slug_generator(self)
		if self.is_confirmed and self.status == CampaignStatus.NOT_CONFIRMED:
			self.status = CampaignStatus.RUNNING
		else:
			pass
		super(Campaign, self).save(*args, **kwargs)


class Sign(models.Model):
	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	valid = models.BooleanField(default=True) # sign is valid or not

	class Meta:
		unique_together = ["campaign", "owner"]
		
