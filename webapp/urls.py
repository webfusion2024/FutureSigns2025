from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import IndexView,ContactView,PortfolioView,AboutView,ServiceView,SignageView,DesignView,FabricationView,EventServicesView

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('about', AboutView.as_view(), name='about-page'),
    path('contact-us', ContactView.as_view(), name='contact-page'),
    path('service', ServiceView.as_view(), name='service-page'),
    path('signage', SignageView.as_view(), name='signage-page'),
    path('print-design', DesignView.as_view(), name='print-design'),
    path('fabrication-engraving', FabricationView.as_view(), name='fabrication-engraving'),
    path('supporteEventServices', EventServicesView.as_view(), name='Support-EventServices'),
    path('portfolio', PortfolioView.as_view(), name='portfolio-page'),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

