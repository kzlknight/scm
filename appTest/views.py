from django.shortcuts import HttpResponse
from appSite.models import Nav
from appSite.serializers import NavSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

class IsLogin(BasePermission):
    message = '未登录'

    def has_permission(self, request, view):
        return True


class V1(APIView):
    permission_classes = [IsLogin]
    def get(self, request, format=None):
        # id = self.request.query_params.get('id', 1)
        #
        # navs = Nav.objects.filter(id=id)
        # nav_serializer = NavSerializer(navs, many=True)
        return Response([{'a':True}])


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='uploads/11.pdf')