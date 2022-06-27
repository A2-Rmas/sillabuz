from django.urls import include, path

from ..views import blog

urlpatterns = [
    path(
        "", 
        blog.ListView.as_view(),
        name="home"
    ),
    path(
        "blog/",
        include(
            (
                [
                    path("", blog.ListView.as_view(), name="list"),
                    path("<int:pk>/detail", blog.DetailView.as_view(), name="detail"),

                ],
                "blog",
            ),
            namespace="blog",
        ),
    ),

]