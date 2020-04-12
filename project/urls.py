"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView
from material.frontend import urls as frontend_urls
import environ


def get_grafana_url():
    env = environ.Env()
    domain = env("GRAFANA_URL", default="localhost:3000")
    token = env("DASHBOARD_TOKEN", default="OMynCUCWz")
    general_dashboard = f"http://{domain}/d/{token}/capacidade-hospitalar?orgId=1"
    return general_dashboard


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("dashboard/", RedirectView.as_view(url=get_grafana_url()), name="grafana"),
    path("", RedirectView.as_view(url="./app/"), name="home"),
    path("", include(frontend_urls)),
    path("", include("django_prometheus.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
