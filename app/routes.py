from fastapi import APIRouter, HTTPException
from app.services import account
from app.models import Event
from fastapi.responses import JSONResponse, Response
router = APIRouter()

@router.post("/reset")
def post_reset():
    response = account.reset()
    if response is None:
        return Response(content="0", status_code=404)
    return Response(content="OK", status_code=200)

@router.get("/balance", response_model=int)
def get_balance(account_id: str):
    balance = account.get_balance(account_id)
    if balance == 0:
        return Response("0", status_code=404)
    return JSONResponse(content=balance, status_code=200)


@router.post("/event")
def post_event(event: Event):
    """Processa eventos de depósito, saque e transferência."""
    response = account.process_event(event)
    if response is None:
        return Response("0", status_code=404)
    return JSONResponse(content=response, status_code=201)


