from django.urls import path
from . import views


handler500 = views.my_customized_server_error


urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('trial/', views.TrialView.as_view(), name='trial'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('team/college/', views.TeamCollegeView.as_view(), name='college'),
    path('team/club/', views.TeamClubView.as_view(), name='club'),
    path('team/national/', views.TeamNationalView.as_view(), name='national'),
    path('team/national/<year>/', views.TeamNationalView.as_view(), name='national'),
    path('training/', views.TrainingView.as_view(), name='training'),
    path('training/jfsa/', views.TrainingJfsaView.as_view(), name='training_jfsa'),
    path('training/story/', views.TrainingStoryView.as_view(), name='training_story'),
    path('race/', views.RaceView.as_view(), name='race'),
    path('race/jfsa/', views.RaceJfsaView.as_view(), name='race_jfsa'),
    path('race/jfsa/', views.RaceOnlineView.as_view(), name='race_online'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about/finswimming/', views.AboutFinView.as_view(), name='about_finswimming'),
    path('about/jfsa/', views.AboutJfsaView.as_view(), name='about_jfsa'),
]
