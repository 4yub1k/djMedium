from django.urls import path
from head.views import Heading

urlpatterns = [
    path("", Heading.as_view(template_name="head/head.html"), name="head"),
]
