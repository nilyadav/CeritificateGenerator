from django.urls import path
from . import views

app_name = "user_management_app"   


urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),
    path('',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/',views.SignupPage,name='signup'),
    # path('render_pdf_view/',views.render_pdf_view,name='render_pdf_view')
    path('rednder_pdf_view/',views.GeneratePdf.as_view(),name='render_pdf_view')

]
