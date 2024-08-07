"""Travel_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from travel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('travel.urls')),
    path('',views.home,name="blog"),
    path('search_by/',views.search_by),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('admin_edit_profile/<int:user_id>/',views.admin_edit_profile),
    path('admin_view_profile/<int:user_id>/',views.admin_view_profile),
    path('admin_view_feedback/',views.admin_view_feedback,name="admin_view_feedback"),
    path('admin_view_destination/',views.admin_view_destination,name="admin_view_destination"),
    path('admin_add_destination/',views.admin_add_destination,name="admin_add_destination"),
    path('admin_edit_destination/<int:cus_id>/',views.admin_edit_destination),
    path('admin_delete_destination/<int:cus_id>/',views.admin_delete_destination),
    path('admin_view_user/',views.admin_view_user,name="admin_view_user"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_view_booking/<int:user_id>/',views.admin_view_booking),
    path('admin_booking_status_confirm/<int:user_id>/<int:b_id>/',views.admin_booking_status_confirm),
    re_path(r'^.*/$', views.custom_404_view),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
