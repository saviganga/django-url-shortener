
# https://www.revsys.com/tidbits/using-different-read-and-write-serializers-django-rest-framework/


class ReadWriteSerializerMixin(object):

    # serializer class to be declared in viewset
    read_serializer_class = None
    write_serializer_class = None


    def get_serializer_class(self):

        """
        Depending on the method in the request, this method returns the appropriate serializer
        """

        if self.request.method.lower() in ["post", "put", "patch", "delete"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a 'read_serializer_class' attribute"
            "or override the 'get_read_serializer_class()' method"
        )

        # return the read_serializer_class attribute
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            f"{self.__class__.__name__} should either include a 'write_serializer_class' attribute"
            "or override the 'get_write_serializer_class()' method"
        )

        # return the write_serializer_class attribute
        return self.write_serializer_class
