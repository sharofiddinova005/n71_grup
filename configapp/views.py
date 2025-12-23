from django.conf import settings
from django.core.mail import send_mail
from django.db.transaction import commit
from django.shortcuts import render

from django.shortcuts import render
from pyexpat.errors import messages

from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class ActorAPI(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class CommitAPI(ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    queryset = CommitMovie.objects.all()
    serializer_class = CommitSerializer


class MovieAPI(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CommitApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=CommitSerializer)
    def post(self, request):
        serializer = CommitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(data=serializer.data)

    def get(self, request):
        commits=CommitMovie.objects.filter()


class SendEmailApi(APIView):
    @swagger_auto_schema(request_body=SendEmailSerializer)
    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']  # yuboriladigan email
            text = serializer.validated_data['text']  # xabar matni

            subject = "Ustozdan!"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]  # foydalanuvchi tomonidan berilgan email

            send_mail(subject, text, email_from, recipient_list)

            return Response(data={f'{email}': "yuborildi"})

        return Response(serializer.errors)



