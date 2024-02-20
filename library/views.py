from django.utils.timezone import now
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response

from .models import Borrower, BorrowRecord
from .serializers import BorrowerSerializer, BorrowRecordSerializer


class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    permission_classes = [DjangoModelPermissions]


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return self.queryset

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')

    @action(methods=['GET'], detail=True, url_path='return_book')
    def return_book(self, request, pk=None):
        """BorrowRecord"""
        borrow_record = self.get_object()
        if borrow_record.return_date is not None:
            return Response(
                {
                    "BorrowRecord": "this BorrowRecord is already returned"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BorrowRecordSerializer(
            borrow_record,
            data={
                "return_date": now().date(),
            },
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
