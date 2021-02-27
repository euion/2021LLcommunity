from django.urls import path
from . import views

info_url = [
   path('infoList/', views.infoList, name="infoList"),
   path('infoNew/', views.infoNew, name="infoNew"),
   path('infoCreate/', views.infoCreate, name="infoCreate"),
   path('info/<int:info_id>', views.infoDetail, name="infoDetail"),
   path('info/<int:info_id>/delete', views.infoDelete, name="infoDelete"),
   path('info/<int:info_id>/edit', views.infoEdit, name="infoEdit"),

]

qna_url = [
   path('qnaList/', views.qnaList, name="qnaList"),
   path('qnaCreate/', views.qnaCreate, name="qnaCreate"),
   path('qnaNew/', views.qnaNew, name="qnaNew"),
   path('qna/<int:qna_id>', views.qnaDetail, name="qnaDetail"),
   path('qna/<int:qna_id>/delete', views.qnaDelete, name="qnaDelete"),
   path('qna/<int:qna_id>/edit', views.qnaEdit, name="qnaEdit"),
]

crud_url = [
   path('', views.index, name="index"),
   path('free/', views.free, name="free"),
   path('new/', views.new, name="new"),
   path('create/', views.create, name="create"),
   path('crud/<int:crud_id>', views.detail, name='detail'),
   path('crud/<int:crud_id>/delete', views.delete, name="delete"),
   path('crud/<int:crud_id>/edit', views.edit, name="edit"),
]

comment_url = [
   path('crudComment/', views.crudComment, name="crudComment"),
]

urlpatterns = info_url + qna_url + crud_url + comment_url
