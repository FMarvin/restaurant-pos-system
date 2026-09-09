from sqlalchemy.orm import Session
from ..repositories.order_repository import OrderRepository
from ..schemas import OrderCreate

class OrderService:
    def __init__(self, db: Session):
        self.repository = OrderRepository(db)

    def place_order(self, order_in: OrderCreate):
        table = self.repository.get_table_by_number(order_in.table_number)
        if not table:
            raise ValueError("La mesa no existe.")
        return self.repository.create_order(order_in, table)

    def mark_as_ready(self, order_id: int):
        return self.repository.mark_ready(order_id)

    def process_payment(self, table_number: int):
        return self.repository.pay_and_free_table(table_number)

    def list_kitchen_orders(self):
        return self.repository.get_pending_orders()

    def get_tables(self):
        return self.repository.get_all_tables()

    def get_dishes(self):
        return self.repository.get_dishes()
