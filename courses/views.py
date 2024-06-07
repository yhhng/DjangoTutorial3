from django.http import HttpResponse
from django.template import loader
from .models import Course


def courses(request):
    mycourses = Course.objects.all().values()
    template = loader.get_template("all_courses.html")
    context = {
        "mycourses": mycourses,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    # Retrieve the course by ID from the Course model
    mycourse = Course.objects.get(id=id)

    template = loader.get_template("details.html")

    # Create a context dictionary to pass the course data to the template
    context = {
        "mycourse": mycourse,
    }

    # Render the template with the context and return the HttpResponse
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
