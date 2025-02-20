from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        """
        Render the custom login page.
        """
        return render(request, self.template_name)
    
class AboutView(View):
    template_name = "about/about.html"

    def get(self, request):
        """
        Render the custom about page.
        """
        return render(request, self.template_name)
    
class ContactView(View):
    template_name = "contact/contact.html"

    def get(self, request):
        """
        Render the custom contact page.
        """
        return render(request, self.template_name)

class ServiceView(View):
    template_name = "service/service.html"

    def get(self, request):
        """
        Render the custom Service page.
        """
        return render(request, self.template_name)
    
class SignageView(View):
    template_name = "service/signage.html"

    def get(self, request):
        """
        Render the custom Service page.
        """
        return render(request, self.template_name)
    
class DesignView(View):
    template_name = "service/print_design.html"

    def get(self, request):
        """
        Render the custom Service page.
        """
        return render(request, self.template_name)

class FabricationView(View):
    template_name = "service/fabrication_engraving.html"

    def get(self, request):
        """
        Render the custom Service page.
        """
        return render(request, self.template_name)

class EventServicesView(View):
    template_name = "service/support_eventservices.html"

    def get(self, request):
        """
        Render the custom Service page.
        """
        return render(request, self.template_name)

class PortfolioView(View):
    template_name = "portfolio/portfolio.html"

    def get(self, request):
        """
        Render the custom portfolio page.
        """
        return render(request, self.template_name)