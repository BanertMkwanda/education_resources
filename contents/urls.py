# Defining urls for contents

from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
	# url for homepage
	path('', views.index, name='index'),
	# primary or secondary
	path('education_levels', views.education_levels, name='education_levels'),
	# Junior or Secondary
	path('class_levels/<int:education_level_id>/', views.class_levels, name='class_levels'),
	# class like Standard 1, Form 4
	path('grades/<int:class_level_id>/', views.grades, name='grades'),
	# Subject that user is looking for
	path('subjects/<int:grade_id>/', views.subjects, name='subjects'),
	# resource type like book, pamphlets
	path('resource_types/<int:subject_id>/', views.resource_types, name='resource_types'),
	# Showing document of book, pamphlet on different pages
	path('documents_short_info/<int:resource_type_id>/', views.documents_short_info, name='documents_short_info'),
	# Showing full info of book or pamphlet
	path('document/<int:document_id>/', views.document, name='document'),
	# url for downloading url
	path('download/<int:document_id>/', views.download, name='download'),
]