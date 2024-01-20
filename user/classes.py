from . import models
from . import serializers


class Section:
    """
    "Section CRUD operations
    """
    def __init__(self,request=None):
        if not request:
            raise AssertionError(f"Request Object is not provided")
        self.request = request

    def addSection(self):
        list=['name']
        for params in list:
            if not self.request.data.get(params):
                raise AssertionError(f"Please provide {params.replace('_',' ').title()}")
        try:
            section = models.Section.objects.create(
                name = self.request.data.get('name'),
            )
        except:
            raise AssertionError('Section already exists')

        section_serializer = serializers.SectionSerializer(section).data
        return section_serializer

    def listSection(self):
        offset = self.request.data.get("offset",0)
        limit = self.request.data.get("limit",10)

        count = models.Section.objects.filter().count()

        section = models.Section.objects.filter()[offset:offset+limit]
        section_serializer = serializers.SectionSerializer(section,many=True).data
        return count,section_serializer

    def getSection(self,id):
        if not id:
            raise AssertionError(f"Section Id is not provided")

        section = models.Section.objects.filter(id=id)

        if section:
            section_serializer = serializers.SectionSerializer(section[0]).data
            return section_serializer
        
        return None

    def updateSection(self,id=None):
        if not id:
            raise AssertionError(f"Section Id is required to perform this action.")
        
        section = models.Section.objects.filter(id=id)

        if not section.exists():
            raise AssertionError(f"Invalid section id")

        section = section[0]
        section_serializer = serializers.SectionSerializer(section,data=self.request.data,partial=True)
        if section_serializer.is_valid():
            section_serializer.save()
            return section_serializer.data
        else:
            return section_serializer.errors
       
    def deleteSection(self,id=None):
        if not id:
            raise AssertionError(f"SectionId is required to perform this action")

        section = models.Section.objects.filter(id=id)
        if not section.exists():
            raise AssertionError(f'Invalid section Id')
        
        section = models.Section.objects.filter(id=id).delete()
        return

class Student:
    """
    "Student CRUD operations
    """
    def __init__(self,request=None):
        if not request:
            raise AssertionError(f"Request Object is not provided")
        self.request = request

    def addStudent(self):
        list=['name','section_id']
        for params in list:
            if not self.request.data.get(params):
                raise AssertionError(f"Please provide {params.replace('_',' ').title()}")
        
        section = models.Section.objects.filter(id=self.request.data.get('section_id'))

        if not section:
            raise AssertionError(f"provide valid Section id")

        student = models.Student.objects.create(
            name = self.request.data.get('name'),
            section = section[0],
        )

        student_serializer = serializers.SectionSerializer(student).data
        return student_serializer

    def getStudent(self,id):
        if not id:
            raise AssertionError(f"Student Id is not provided")

        student = models.Student.objects.filter(id=id)

        if student:
            student_serializer = serializers.StudentSerializer(student[0]).data
            return student_serializer
        
        return None
            
    def updateStudent(self,id=None):
        if not id:
            raise AssertionError(f"student Id is required to perform this action.")
        
        student = models.Student.objects.filter(id=id)
        if not student.exists():
            raise AssertionError(f"Invalid student id")

        data = {}
        if self.request.data.get('section_id'):
            section = models.Section.objects.filter(id=self.request.data.get('section_id'))
            if not section.exists():
                raise AssertionError(f"Invalid section id")
            data['section'] = self.request.data.get('section_id')

        student = student[0]
        data['name'] = self.request.data.get('name')
        
        student_serializer = serializers.StudentSerializer(student,data=data,partial=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return student_serializer.data
        else:
            return student_serializer.errors
       
    def deleteStudent(self,id=None):
        if not id:
            raise AssertionError(f"StudentId is required to perform this action")

        student = models.Student.objects.filter(id=id)
        if not student.exists():
            raise AssertionError(f'Invalid student Id')
        
        student = models.Student.objects.filter(id=id).delete()
        return

class StudentSection:
    def __init__(self,request=None):
        if not request:
            raise AssertionError(f"Request Object is not provided")
        self.request = request

    def listStudentFromSection(self,section_id):
        if not id:
            raise AssertionError(f"Section Id is not provided")
        
        student = models.Student.objects.filter(section_id=section_id)

        student_data = serializers.StudentSerializer(student,many=True).data
        return student_data