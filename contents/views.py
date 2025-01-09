from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import EducationLevel, ClassLevel, Grade, Subject, ResourceType, Document
from django.http import FileResponse

def index(request):
	# Home page
	return render(request, 'contents/index.html')

def education_levels(request):
	# Primary or Secondery level
	education_levels = EducationLevel.objects.order_by('text')
	context = {'education_levels': education_levels}

	return render(request, 'contents/education_levels.html', context)

def class_levels(request, education_level_id):
	# Showing each education level on seperate pages and it's class levels.
	education_level = EducationLevel.objects.get(id=education_level_id)
	class_levels = education_level.classlevel_set.order_by('text')

	context = {'education_level': education_level, 'class_levels': class_levels}
	return render(request, 'contents/class_levels.html', context)

def grades(request, class_level_id):
	# Showing each class level on seperate page and it's classes.
	class_level = ClassLevel.objects.get(id=class_level_id)
	grades = class_level.grade_set.order_by('date_added')

	context = {'class_level': class_level, 'grades': grades}
	return render(request, 'contents/grades.html', context)

def subjects(request, grade_id):
	# Showing each class or grade like form 2 and its subjects on seperate page.
	grade = Grade.objects.get(id=grade_id)
	subjects = grade.subject_set.order_by('text')

	context = {'grade': grade, 'subjects': subjects}
	return render(request, 'contents/subjects.html', context)

def resource_types(request, subject_id):
	# Showing each subject on seperate page and its resource type like book, pamphlet
	subject = Subject.objects.get(id=subject_id)
	resource_types = subject.resourcetype_set.order_by('date_added')

	context = {'subject': subject, 'resource_types': resource_types}
	return render(request, 'contents/resource_types.html', context)

def documents_short_info(request, resource_type_id):
 	# Showing each resource type like book, pamphlet on seperate with its document
 	resource_type = ResourceType.objects.get(id=resource_type_id)
 	documents = resource_type.document_set.order_by('caption')
 	
 	context = {'documents': documents}
 	return render(request, 'contents/documents_short_info.html', context)

def document(request, document_id):
	# Showing full info of book or pamphlet
	document = Document.objects.get(id=document_id)

	context = {'document': document}
	return render(request, 'contents/document.html', context)

def download(request, document_id):
	document = get_object_or_404(Document, pk=document_id)
	file_path = document.uploaded_document.path 
	response = FileResponse(open(file_path, 'rb'))
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = f'attachment; filename="{document.caption}.pdf"'
	return response





 	



