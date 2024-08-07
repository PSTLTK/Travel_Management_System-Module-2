from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from travel import views

urlpatterns = [
    path('contact/<int:user_id>/',views.contact),
    path('feedback/',views.feedback,name="feedback"),
    path('view_destination/',views.view_destination,name="view_destination"),
    path('detail_destination/<int:cus_id>/',views.detail_destination),
    path('asia/',views.asia,name="asia"),
    path('africa/',views.africa,name="africa"),
    path('northamerica/',views.northamerica,name="northamerica"),
    path('southamerica/',views.southamerica,name="southamerica"),
    path('europe/',views.europe,name="europe"),
    path('australia/',views.australia,name="australia"),
    path('antarctica/',views.antarctica,name="antarctica"),
    path('edit_profile/<int:user_id>/',views.edit_profile),
    path('view_profile/<int:user_id>/',views.view_profile),
    path('change_password/',views.PasswordChangeView.as_view(template_name="change_password.html"),name="change_password"),
    path('password_success/',views.password_success,name="password_success"),
    path('booking/<int:cus_id>/',views.booking),
    path('booking_success/<int:cus_id>/<int:b_id>/',views.booking_success),
    path('booking_cancel/<int:user_id>/<int:b_id>/',views.booking_cancel),
    path('mybooking/<int:user_id>/',views.mybooking),
]
