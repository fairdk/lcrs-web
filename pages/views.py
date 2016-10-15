from django.views.generic.edit import CreateView


from . import models
from django.shortcuts import redirect
from django.contrib import messages


class MailingListSignup(CreateView):
    
    model = models.MailingListSignup
    fields = ('email',)
    template_name = "pages/mailing_list_signup.html"
    
    def form_valid(self, form):
        form.save()
        
        messages.success(self.request, "Thanks for signing up :)")
        
        return redirect("/")
