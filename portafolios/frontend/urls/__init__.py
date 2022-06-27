from django.urls import path, include

from . import storefront

urlpatterns = [
    path("", include((storefront.urlpatterns, "storefront"), namespace="storefront")),
    # path("storefront/", include((storefront.urlpatterns, "storefront"), namespace="storefront"))
]

