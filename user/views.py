from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
import json
from .classes import Student,Section,StudentSection

# Create your views here.
class SectionView(APIView):
    """
    Section Operations
    """
    def post(self,request,format="json"):
        try:
            section = Section(request)
            section_data = section.addSection()
            data = {}
            data["statusCode"] = 200
            data["msg"] = "Section added succesfully"
            data['data'] = section_data
            return HttpResponse(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while adding Section"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

    def get(self,request,id=None,format="json"):
        try:
            if not id:
                section = Section(request)
                count,section_data = section.listSection()
                data = {
                    "StatusCode"    : 200,
                    "msg"           : "Section list fetched succesfully",
                    "count"         : count,
                    "data"          : section_data
                }
                return HttpResponse(json.dumps(data),content_type = 'application/json')
            else:
                section = Section(request)
                section_data = section.getSection(id)
                if section_data:
                    data = {
                        "StatusCode" : 200,
                        "msg"   : "Section data fetched succesfully",
                        "data"  : section_data
                    }
                else:
                    data = {
                        "StatusCode" : 200,
                        "msg"        : "Provide valid ID"
                    }
                return HttpResponse(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while fetching Section"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

    def put(self,request,id=None,format="json"):
        try:
            section = Section(request)
            section_data = section.updateSection(id)
            return HttpResponse(json.dumps(section_data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while updating section"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

    def delete(self,request,id=None,format="json"):
        try:
            section = Section(request)
            section_data = section.deleteSection(id)
            data = {
                "statusCode" : 200,
                "msg" : "Section deleted Successfully"
            }
            return HttpResponse(json.dumps(data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while Deleting Section"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')


class StudentView(APIView):
    """
    Student Operations
    """
    def post(self,request,format="json"):
        try:
            student = Student(request)
            student_data = student.addStudent()
            data = {}
            data["statusCode"] = 200
            data["msg"] = "Student added succesfully"
            data['data'] = student_data
            return HttpResponse(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while adding Student"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

    def get(self,request,id=None,format="json"):
        try:
            student = Student(request)
            student_data = student.getStudent(id)
            if student_data:
                data = {
                    "StatusCode" : 200,
                    "msg"   : "Student data fetched succesfully",
                    "data"  : student_data
                }
            else:
                data = {
                    "StatusCode" : 200,
                    "msg"        : "Provide valid ID"
                }
            return HttpResponse(json.dumps(data),content_type = 'application/json')
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while fetching Student"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

    def put(self,request,id=None,format="json"):
        try:
            student = Student(request)
            student_data = student.updateStudent(id)
            return HttpResponse(json.dumps(student_data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while updating student"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

    def delete(self,request,id=None,format="json"):
        try:
            student = Student(request)
            student_data = student.deleteStudent(id)
            data = {
                "statusCode" : 200,
                "msg" : "student deleted Successfully"
            }
            return HttpResponse(json.dumps(data),content_type="application/json")
        except (AssertionError) as ex:
            data = {
                "statusCode" : 400,
                "msg" : ex.args[0] if ex.args[0] else "Something went wrong while Deleting Student"
            }
            return HttpResponse(json.dumps(data),content_type = 'application/json')

class StudentSectionView(APIView):
    def get(self,request,id=None,format="json"):
        student = StudentSection(request)
        student_data = student.listStudentFromSection(id)
        data = {
            "StatusCode"    : 200,
            "msg"           : "Student Section wise listed succesfully",
            "data"          : student_data
        }
        return HttpResponse(json.dumps(data),content_type = 'application/json')