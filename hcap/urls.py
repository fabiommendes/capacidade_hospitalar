from django.conf import settings
from django.urls import path, include
from django.utils.translation import gettext as __

from hcap import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path(
        __("request-authorization/"), views.request_authorization_view, name="request_authorization"
    ),
    path(__("my-authorizations/"), views.my_authorizations_view, name="my_authorizations"),
    path(__("my-authorizations/manager/"), include(views.MyManagerAuthorizationsViewSet().urls)),
    path(__("my-authorizations/notifier/"), include(views.MyNotifierAuthorizationsViewSet().urls)),
    # path("capacidade/", include(views.CapacityViewSet().urls)),
    # path("diario/", include(views.LogEntryViewSet().urls)),
    # path(
    #     "historico-de-notificacoes/",
    #     views.notification_history_view,
    #     name="notification_history",
    # ),
    # path("monitor", views.monitor_view),
    # path("notificadores-pendentes/", include(views.NotifierPendingApprovalViewSet().urls)),
    # path("unidade-de-saude/", include(views.HealthcareUnitViewSet().urls)),
    # path(
    #     "vis/units/<int:cnes_id>/capacity.svg",
    #     views.plot_healthcare_unit_capacity,
    #     name="capacity_plot",
    # ),
]
