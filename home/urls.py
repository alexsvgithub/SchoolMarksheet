import imp
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("marksheet", views.marksheet, name='marksheet'),
    path("Details", views.Details, name='Details'),
    path("Login", views.Login, name='Login'),
    path("logout_user", views.logout_user, name='logout_user'),
    path("PlayingGround", views.PlayingGround, name='PlayingGround'),
    path("EditableDetails", views.EditableDetails, name='EditableDetails'),
    path("EditableMarksheet", views.EditableMarksheet, name='EditableMarksheet'),
    path("EntrySplitter", views.EntrySplitter, name='EntrySplitter'),
    path("saveMarksheet", views.saveMarksheet, name='saveMarksheet'),
    
]
