from django.shortcuts import render

from rest_framework import generics
from .models import Alert
from .serializers import AlertSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.contrib.auth.models import User
from notifications.util import send_notification_to_user


class AddAlertView(generics.CreateAPIView):
    serializer_class = AlertSerializer
    parser_classes = [MultiPartParser, FormParser]
    def perform_create(self, serializer):
        serializer.save()
        admins = User.objects.all()

        if admins.exists():
            message = "New Eco Alert"
            for admin in admins:
                send_notification_to_user(admin.id, message)


class AllAlertsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        alerts = Alert.objects.all().order_by("-created_at")
        if not alerts:
            return Response({"message": "No alerts records found."}, status=404)
        serializer = AlertSerializer(alerts, many=True,context={'request': request})
        return Response(serializer.data)


   

class UpdateAlertStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        
        reportId = request.data.get("reportId")
        newStatus = request.data.get("newStatus")
        

        if not reportId or not newStatus:
            return Response({"error": "reportId and newStatus are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        report = Alert.objects.get(id=reportId)

        if not report:
            return Response({"error": "report not found."},
                            status=status.HTTP_404_BAD_REQUEST)
        
        valid_statuses = [choice[0] for choice in Alert.STATUS_CHOICES]
        if newStatus not in valid_statuses:
            return Response(
                    {"error": f"Invalid status. Allowed values are: {', '.join(valid_statuses)}"},
                    status=status.HTTP_400_BAD_REQUEST
            )

        report.status = newStatus
        report.save()
        return Response({"message": "report updated successfully."},
                        status=status.HTTP_200_OK)
    
