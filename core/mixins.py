from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages

class AnonymousMixin(AccessMixin):

    def handle_no_permission(self):
        messages.warning(request, "You are not allowed in this page")
        return redirect(self.request.META["HTTP_REFERER"])

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
