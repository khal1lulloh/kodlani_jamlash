from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'index.html' 
class PageView(TemplateView):
	template_name='home.html'
class AboutPageView(TemplateView):
	template_name='about.html'
class WorksPageView(TemplateView):
	template_name='works.html'
class JournalPageView(TemplateView):
	template_name='journal.html'
class ContactsPageView(TemplateView):
	template_name='contacts.html'