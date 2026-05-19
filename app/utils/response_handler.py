from fastapi.responses import JSONResponse

def success_response(data, message="Success"):
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": message,
            "data": data
        }
    )