import json
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def foo(request):
    data = {
        "message": "Hello django"
    }

    return HttpResponse(
       content_type="application/json",
       content=json.dumps(data)
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("foo/", foo),
]
