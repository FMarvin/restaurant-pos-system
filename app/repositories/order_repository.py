from sqlalchemy.orm import Session
from ..models import RestaurantTable, Order, OrderItem, Dish, TableStatus, OrderStatus
from ..schemas import OrderCreate

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_table_by_number(self, number: int):
        return self.db.query(RestaurantTable).filter(RestaurantTable.number == number).first()

    def get_all_tables(self):
        return self.db.query(RestaurantTable).order_by(RestaurantTable.number).all()

    def get_dishes(self):
        return self.db.query(Dish).all()

    def create_order(self, order_data: OrderCreate, table: RestaurantTable):
        total = 0.0
        new_order = Order(
            table_id=table.id,
            special_instructions=order_data.special_instructions,
            status=OrderStatus.PENDING.value
        )
        self.db.add(new_order)
        self.db.flush()

        for item in order_data.items:
            dish = self.db.query(Dish).filter(Dish.id == item.dish_id).first()
            if dish:
                total += float(dish.price) * item.quantity
                order_item = OrderItem(order_id=new_order.id, dish_id=dish.id, quantity=item.quantity)
                self.db.add(order_item)

        new_order.total = total
        table.status = TableStatus.OCCUPIED.value
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def get_pending_orders(self):
        return self.db.query(Order).filter(Order.status == OrderStatus.PENDING.value).all()

    def mark_ready(self, order_id: int):
        order = self.db.query(Order).filter(Order.id == order_id).first()
        if order:
            order.status = OrderStatus.READY.value
            self.db.commit()
            self.db.refresh(order)
        return order

    def pay_and_free_table(self, table_number: int):
        table = self.get_table_by_number(table_number)
        if not table:
            return None
        orders = self.db.query(Order).filter(
            Order.table_id == table.id, 
            Order.status.in_([OrderStatus.PENDING.value, OrderStatus.READY.value])
        ).all()
        for o in orders:
            o.status = OrderStatus.PAID.value
        table.status = TableStatus.FREE.value
        self.db.commit()
        return table
