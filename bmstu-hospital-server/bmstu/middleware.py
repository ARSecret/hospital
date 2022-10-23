def allow_cors_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5173'
        return response
    return middleware