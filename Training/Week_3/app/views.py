from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
from django.core.paginator import Paginator
import json

def home(request):
    page_number = request.GET.get("page", 1)

    students = Student.objects.all().order_by("id")
    paginator = Paginator(students, 50)
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"students": page_obj})


def ajax_submit(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            student = Student.objects.create(name=data.get("name"),age=data.get("age"),email=data.get("email"),phone=data.get("phone"),address=data.get("address"),)
            return JsonResponse({"message": "Student added successfully"})

        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)

    return JsonResponse({"message": "Invalid request"}, status=400)


def ajax_delete(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = Student.objects.get(id=data.get("id"))
            student.delete()

            return JsonResponse({"message": "Student deleted successfully"})

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student not found"}, status=404)

    return JsonResponse({"message": "Invalid request"}, status=400)


def ajax_edit(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = Student.objects.get(id=data.get("id"))
            return JsonResponse({"name": student.name,"age": student.age,"email": student.email,"phone": student.phone,"address": student.address})

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student not found"}, status=404)

    return JsonResponse({"message": "Invalid request"}, status=400)

def ajax_update(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = Student.objects.get(id=data.get("id"))

            student.name = data.get("name")
            student.age = data.get("age")
            student.email = data.get("email")
            student.phone = data.get("phone")
            student.address = data.get("address")
            student.save()

            return JsonResponse({"message": "Student updated successfully"})

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student not found"}, status=404)

        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)

    return JsonResponse({"message": "Invalid request"}, status=400)