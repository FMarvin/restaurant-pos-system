from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.order_service import OrderService
from ..schemas import OrderCreate
from ..websocket_manager import ConnectionManager, get_ws_manager

router = APIRouter(prefix="/api/orders", tags=["Orders"])

def get_order_service(db: Session = Depends(get_db)) -> OrderService:
    return OrderService(db)

@router.get("/kitchen")
def get_kitchen_orders(service: OrderService = Depends(get_order_service)):
    orders = service.list_kitchen_orders()
    return [
        {
            "id": o.id,
            "table_number": o.table.number,
            "special_instructions": o.special_instructions,
            "items": [{"dish": i.dish.name, "quantity": i.quantity} for i in o.items]
        }
        for o in orders
    ]

@router.post("")
async def create_order(
    payload: OrderCreate,
    service: OrderService = Depends(get_order_service),
    ws: ConnectionManager = Depends(get_ws_manager)
):
    try:
        order = service.place_order(payload)
        await ws.broadcast({
            "event": "NEW_ORDER",
            "order": {
                "id": order.id,
                "table_number": order.table.number,
                "special_instructions": order.special_instructions,
                "items": [{"dish": i.dish.name, "quantity": i.quantity} for i in order.items]
            }
        })
        return {"status": "success", "order_id": order.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{order_id}/ready")
async def set_order_ready(
    order_id: int,
    service: OrderService = Depends(get_order_service),
    ws: ConnectionManager = Depends(get_ws_manager)
):
    order = service.mark_as_ready(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    await ws.broadcast({
        "event": "ORDER_READY",
        "order_id": order.id,
        "table_number": order.table.number
    })
    return {"status": "success"}
