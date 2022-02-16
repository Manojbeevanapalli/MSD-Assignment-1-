from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

app_name = 'journey'

urlpatterns = [
                  path('', views.post_list, name='post_list'),
                  path('post_list', views.post_list, name='post_list'),
                  path('signup', views.signup, name='signup'),
                  path('post_detail', views.post_detail, name='post_detail'),
                  path('post/create/', views.post_new, name='post_new'),
                  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
                  path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
                  path('comment_list', views.comment_list, name='comment_list'),
                  path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
                  path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
                  path('travelblog_post/<int:post_id>', views.travelblog_post, name='travelblog_post'),

                  path('accounts/password_reset/',
                       auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
                       name='password_reset'),
                  path('accounts/password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_email_sent.html"),
                       name='reset_email_sent'),
                  path('accounts/reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_confirm.html"),
                       name='reset_confirm'),
                  path('accounts/reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(template_name="registration/reset_complete.html"),
                       name='reset_complete'),

                  path('accounts/password_change/',
                       auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),
                       name='password_change'),
                  path('accounts/password_change/done/',
                       auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_changed.html"),
                       name='password_changed'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
