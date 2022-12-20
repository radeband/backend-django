from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="Radeband",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Radeband API Doc.",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/account/', include('account.routes.v1')),
    path('v1/', include('company.urls_v1')),

    # swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
