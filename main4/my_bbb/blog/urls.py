from django.urls import path
from . import views
from django.urls import path
from .views import DeleteComment



urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_like'),
               path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
               path('delete_comment/<int:comment_id>/', DeleteComment.as_view(), name='delete_comment')]