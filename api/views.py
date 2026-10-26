from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import student, book
from .serializers import student_serialzer, book_ser
from django.shortcuts import get_object_or_404

class create(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = student_serialzer(data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                return Response({"Error" : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
            return Response({"Message" : "Saved"}, status=status.HTTP_200_OK)
        except Exception as e: 
            return Response({"Error" : str(e)}, status=status.HTTP_200_OK)
        
class list(APIView):
    def get(self, request):
        try:
            serializer = student_serialzer(student.objects.all(), many = True)
            return Response({"Message" : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e: 
            return Response({"Error" : str(e)}, status=status.HTTP_200_OK)
        
class retrive(APIView):
    def get(self, request, pk = None):
        try:
            print(f"request.query_params()",request.query_params.get("id") )
            queryset = student.objects.get(pk = pk)
            serializer = student_serialzer(queryset)
            return Response({"Message" : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e: 
            print(e.__traceback__.tb_lineno)
            return Response({"Error" : str(e)}, status=status.HTTP_200_OK)
        
class delete(APIView):
    def delete(self, request, pk = None):
        try:
            queryset = get_object_or_404(student, id=pk)
            queryset.delete()
            return Response({"Message" : "Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e.__traceback__.tb_lineno) 
            return Response({"Error" : str(e)}, status=status.HTTP_200_OK)
        
        
class partial_update(APIView):
    def patch(self, request, pk = None):
        try:
            queryset = get_object_or_404(student, id=pk)
            serializer = student_serialzer(queryset, data = request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({"Error" : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
            return Response({"Message" : "Updated partialiy"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e.__traceback__.tb_lineno) 
            return Response({"Error" : str(e)}, status=status.HTTP_200_OK)
        
        

from django.shortcuts import render

def student_form_view(request):
    return render(request, "studentapp/student_form.html")


class books(APIView):
    def get(self, request):
        books = book.objects.all()
        serializer = book_ser(books,many = True)
        return Response({"books" : serializer.data}, status=200)
    
    
# comments

        
        

            
        


