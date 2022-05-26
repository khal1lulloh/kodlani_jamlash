from django.urls import path
from .views import HomePageView,PageView,AboutPageView,WorksPageView,JournalPageView,ContactsPageView

urlpatterns = [
	path('',HomePageView.as_view(),name = 'index'),
	path('home/',PageView.as_view(),name = 'home'),
	path('about/',AboutPageView.as_view(),name='about'),
	path('works/',WorksPageView.as_view(),name='works'),
	path('journal/',JournalPageView.as_view(),name='journal'),
	path('contacts/',ContactsPageView.as_view(),name='contacts'),
	]