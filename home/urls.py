from django.urls import path
from  . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('report',views.report,name='report'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("profile/", views.user_profile, name= "profile"),
    path("show-reports/", views.show_reports, name= "show_reports"),
    #  path("download/<int:id>", views.some_view, name= "download"),
    #  path('test/<int:id>/',views.render_pdf_view,name="test"),
    path('pdf/<pk>/',views.victim_render_pdf_view,name="victim-pdf-viewer"),
    path('accept-term',views.AcceptTerm.as_view(),name='accept-term'),
    path('method-to-report',views.MethodToReport.as_view(),name='method-to-report'),

]
