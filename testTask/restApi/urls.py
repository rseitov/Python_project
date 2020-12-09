from django.urls import path, re_path
from restApi import views

urlpatterns = [
    path('get-all-directories', views.get_all_directories),
    path('get-all-dirs-with-elements', views.get_all_dirs_with_elements),
    path('get-by-date/<date>', views.get_by_date),
    path('get-by-id/<id>', views.get_by_id),
    path('get-by-version/<ver>', views.get_version),

    path('post-new-dir', views.post_new_dir),


    path('test-func', views.test_func)
]