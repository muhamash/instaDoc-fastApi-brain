from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def test_root():
    return {
        "message": "Service is running successfully! Please navigate --> /api/v1 endpoint",
        "status": "ok",
    }
