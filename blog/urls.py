from django.urls import path
from blog import views

app_name='blog'

urlpatterns=[
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_edit, name='post_edit'),
    path('draft/', views.post_draft_list, name ='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # url(r'^search/$',views.post_search, name='post_search'),
     # url(r'^post/(?P<pk>\d+)/comment/$', views.PostDetail.add_comment_to_post, name='add_comment_to_post'),
]