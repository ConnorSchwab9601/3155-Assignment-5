from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, order_id: int, sandwich_id: int, amount: int):
    order_detail = models.OrderDetail(
        order_id=order_id, 
        sandwich_id=sandwich_id, 
        amount=amount)
    db.add(order_detail)
    db.commit()
    db.refresh(order_detail)
    return order_detail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail_id: int, amount: int):
    order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if order_detail:
        order_detail.amount = amount
        db.commit()
        db.refresh(order_detail)
    return order_detail


def delete(db: Session, order_detail_id):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)