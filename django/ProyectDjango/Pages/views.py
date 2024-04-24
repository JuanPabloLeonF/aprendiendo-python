from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Pages import models

@login_required(login_url="logingPage")
def page(request, slug):
    page = models.Page.objects.get( slug=slug )
    context = {
        "page": page
    }
    return render(request, "pages/page.html", context)