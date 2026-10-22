import json
from django.http import JsonResponse

sensitive_keys = ["api-key","apikey","api_key","password","pass"]

# def get_request_payload(request):A
#     content_type = request.META.get("CONTENT_TYPE", "")

#     # JSON
#     if "application/json" in content_type:
#         try:
#             body = request.body.decode("utf-8")
#             return json.loads(body) if body else {}
#         except Exception:
#             return {}

#     # Form-data / urlencoded
#     elif "application/x-www-form-urlencoded" in content_type or "multipart/form-data" in content_type:
#         return request.POST.dict()

#     # Fallback
#     elif request.body:
#         try:
#             return json.loads(request.body.decode("utf-8"))
#         except Exception:
#             return {}
#     else:
#         return {}


class restrict_sensative_data:
    def __init__(self, get_Response):
        self.get_Response = get_Response
    
    def __call__(self, request):
        # print(request.GET)
        # print(request.GET.keys())
        # print("Headers")
        # print(request.headers)
        # print(type(request.headers.items()), "lale")
        for key in request.GET.keys():   # worked
            if key.lower() in sensitive_keys:
                print("hiiiiiiiiiiiiii")
                return JsonResponse({"Error":"Sensative info not allowed in Query Params"})
        for key, value in request.headers.items():  # worked
            if key.lower() in sensitive_keys:
                return JsonResponse({"Error":"Sensative info not allowed in Headers"})
            
        if request.method in ["POST", "PUT", "PATCH"]:
            # request.payload = self.get_request_payload(request)
            # print(request.payload )
            # payload = get_request_payload(request)
            # print(f"p is {payload}")
            print(request.content_type, "content type")
            print(request.POST.keys(), "hiiiii")
            data = request.body.decode("utf-8")  # take easily from browser
            
            # data = request.body()
            print(f"decode body is {data}")
            print(repr(data))
            data = json.loads(data)
            if isinstance(data,dict):
                for key, value in data.items():
                    if key.lower() in sensitive_keys:
                        return JsonResponse({"Error" : "Sensative info not allowed in request body"})
            print(data, "\n in middleware")
            print(type(data))
        response = self.get_Response(request)
        print(f"response is {response}")
        return response
    
    
    
    

# import io

# class CopyBodyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Keep a copy of raw body
#         if not hasattr(request, "_body_copy"):
#             request._body_copy = request.body

#         # Now you can decode safely
#         raw_body = request._body_copy.decode("utf-8") if request._body_copy else ""
#         print("Raw Body Copy:", raw_body)

#         response = self.get_response(request)
#         return response
