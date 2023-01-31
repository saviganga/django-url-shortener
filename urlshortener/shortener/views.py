from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from shortener.serializermixin import ReadWriteSerializerMixin

from shortener import models as shortener_models
from shortener import serializers as shortener_serializers
from shortener.utils import randomize_strings
from shortener import responses as shortener_responses

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action




# Create your views here.

class URLShortenerViewSet(ReadWriteSerializerMixin, ModelViewSet):

    queryset = shortener_models.URLShortener.objects.all()
    read_serializer_class = shortener_serializers.ReadURLShortenerSerializer
    write_serializer_class = shortener_serializers.WriteURLShortenerSerializer

    def get_queryset(self):
        return self.queryset.all()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            seriaizer = self.read_serializer_class(queryset, many=True)
            return Response(
                data=shortener_responses.URLShortenerResponses().get_urlshortener_success(data=seriaizer.data),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data=shortener_responses.URLShortenerResponses().get_urlshortener_error(),
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request, *args, **kwargs):

        serializer = self.write_serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as invalid_serializer_error:
            return Response(
                data=shortener_responses.URLShortenerResponses().create_urlshortener_error(data=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        shortened_url = serializer.create(serializer.validated_data)


        headers = self.get_success_headers(serializer.data)
        return Response(data=shortener_responses.URLShortenerResponses().create_urlshortener_success(data=shortened_url), status=status.HTTP_201_CREATED, headers=headers)
        

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception as get_instance_error:
            return Response(
                data=shortener_responses.URLShortenerResponses().retreive_urlshortener_error(),
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.read_serializer_class(instance)

        return Response(
            data=shortener_responses.URLShortenerResponses().retreive_urlshortener_success(serializer.data),
            status=status.HTTP_200_OK
        ) 

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop("partial", False)
            instance = self.get_object()
        except Exception as get_instance_error:
            return Response(
                data=shortener_responses.URLShortenerResponses().update_urlshortener_error(),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.write_serializer_class(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as validate_serializer_error:
            return Response(
                data=shortener_responses.URLShortenerResponses().update_urlshortener_error(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        self.perform_update(serializer)

        return Response(
            data=shortener_responses.URLShortenerResponses().update_urlshortener_success(serializer.data),
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception as get_instance_error:
            return Response(
                data=shortener_responses.URLShortenerResponses().destroy_urlshortener_error(),
                status=status.HTTP_400_BAD_REQUEST
            )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["post"], detail=False,)
    def resolve_original_url(self, request, *args, **kwargs):

        serializer = shortener_serializers.ResolveShortenedURLSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as invalid_serializer_error:
            return Response(
                data=shortener_responses.URLShortenerResponses().resolve_urlshortener_error(serializer.data),
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            shortened_url_object = self.queryset.get(shortened_url=serializer.validated_data.get('shortened_url'))
        except Exception as invalid_shortened_url:
            return Response(
                data=shortener_responses.URLShortenerResponses().resolve_urlshortener_error(),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(
            data=shortener_responses.URLShortenerResponses().resolve_urlshortener_success(shortened_url_object.original_url),
            status=status.HTTP_200_OK
        )




