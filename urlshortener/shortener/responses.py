class URLShortenerResponses():

    def get_urlshortener_success(self, data=None):

         return {
                "status": "SUCCESS",
                "message": "Successully fetched urls",
                "data": data
            }

    def get_urlshortener_error(self, data=None):
        try:
            error_keys = [keyy for keyy in data.keys()]
            return {
                    "status": "FAILED",
                    "message": data[error_keys[0][0]],
                    "data": data
                }
        except Exception:
            return {
                    "status": "FAILED",
                    "message": "Unable to fetch urls",
                }

    def create_urlshortener_success(self, data):


        return {
                "status": "SUCCESS",
                "message": "Successfully shortened url",
                "data": data
            }

    def create_urlshortener_error(self, data=None):
        try:
            error_keys = [keyy for keyy in data.keys()]
            return {
                    "status": "FAILED",
                    "message": data[error_keys[0]][0],
                    "data": data
                }
        except Exception:
            return {
                    "status": "FAILED",
                    "message": "Unable to shorten url",
                }
    
    def retreive_urlshortener_success(self, data):

        return {
                "status": "SUCCESS",
                "message": "Successfully fetched shortened url",
                "data": data
            }

    def retreive_urlshortener_error(self, data=None):
        try:
            error_keys = [keyy for keyy in data.keys()]
            return {
                    "status": "FAILED",
                    "message": data[error_keys[0]][0],
                    "data": data
                }
        except Exception:
            return {
                    "status": "FAILED",
                    "message": "Unable to fetch shortened url",
                }

    def update_urlshortener_error(self, data=None):
        try:
            error_keys = [keyy for keyy in data.keys()]
            return {
                    "status": "FAILED",
                    "message": data[error_keys[0]][0],
                    "data": data
                }
        except Exception:
            return {
                    "status": "FAILED",
                    "message": "Unable to fetch and update shortened url",
                }

    def update_urlshortener_success(self, data):

        return {
                "status": "SUCCESS",
                "message": "Successfully updated shortened url",
                "data": data
            }

    def destroy_urlshortener_error(self, data=None):

        return {
                "status": "FAILED",
                "message": "Unable to fetch shortened url",
            }

    def resolve_urlshortener_success(self, data=None):

         return {
                "status": "SUCCESS",
                "message": "Successully resolved url",
                "data": data
            }

    def resolve_urlshortener_error(self, data=None):
        try:
            error_keys = [keyy for keyy in data.keys()]
            return {
                    "status": "FAILED",
                    "message": data[error_keys[0][0]],
                    "data": data
                }
        except Exception:
            return {
                    "status": "FAILED",
                    "message": "Unable to resolve url",
                }
