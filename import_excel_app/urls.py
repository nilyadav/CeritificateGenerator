from django.urls import path
from . import views
urlpatterns = [
    path('import_excel/',views.import_excel,name="import_excel"),
    path('update_specific_delegates/<int:id>',views.update_specific_delegates,name="update_specific_delegates"),
    path('checked_delegates/',views.checked_delegates,name="checked_delegates"),
    path('search_result/',views.search_result,name="search_result"),
    path('pdf/<int:id>/', views.serve_pdf, name='pdf_file'),
    # path('list_of_delegates/',views.list_of_delegates,name="list_of_delegates"),
    # path('get_checked_list/',views.get_checked_list,name="get_checked_list"),
    # path('specific_pdf_report/<int:id>',views.specific_pdf_report,name="specific_pdf_report"),
    # path('delete_checked_delegates/',views.delete_checked_delegates,name="delete_checked_delegates"),
    # path('find/',views.find,name="find"),
    # path('generate_pdf/',views.render_pdf_view,name="render_to_pdf")

]