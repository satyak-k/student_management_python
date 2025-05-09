from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.utils import timezone  # Import timezone

def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(student_name__icontains=query) | Q(class_name__icontains=query), deleted_at__isnull=True).order_by('student_name')
    else:
        students = Student.objects.filter(deleted_at__isnull=True).order_by('student_name')

    paginator = Paginator(students, 10)  # Show 10 students per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/student_list.html', {'students': students, 'query': query})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk, deleted_at__isnull=True)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk, deleted_at__isnull=True)
    student.soft_delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('student_list')