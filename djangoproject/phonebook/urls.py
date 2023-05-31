from djangoproject.phonebook.views import landing_page, create_contact
from django.urls import path


urlpatterns = [
    path("", landing_page, name="landing-page"),
    path("new-contact", create_contact, name="new-contact"),
]
