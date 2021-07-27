from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns =[
    path('',views.all_blogs,name='blogspot'),
    path('<int:blog_id>/',views.details,name='detail')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)