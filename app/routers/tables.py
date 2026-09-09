from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.order_service import OrderService
from ..websocket_manager import ConnectionManager, get_ws_manager

router = APIRouter(prefix="/api", tags=["Tables & Billing"])

def get_order_service(db: Session = Depends(get_db)) -> OrderService:
    return OrderService(db)

@router.get("/tables")
def get_tables(service: OrderService = Depends(get_order_service)):
    tables = service.get_tables()
    return [{"id": t.id, "number": t.number, "status": t.status} for t in tables]

@router.get("/dishes")
def get_dishes(service: OrderService = Depends(get_order_service)):
    dishes = service.get_dishes()
    return [{"id": d.id, "name": d.name, "price": float(d.price)} for d in dishes]

@router.post("/tables/{number}/pay")
async def pay_and_free(
    number: int,
    service: OrderService = Depends(get_order_service),
    ws: ConnectionManager = Depends(get_ws_manager)
):
    table = service.process_payment(number)
    if not table:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    await ws.broadcast({
        "event": "TABLE_FREED",
        "table_number": number
    })
    return {"status": "paid_and_freed", "table_number": number}
