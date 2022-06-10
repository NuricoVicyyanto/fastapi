from fastapi import APIRouter
from app.api.transactions import create_transaction

api_router = APIRouter(prefix='/api')

api_router.add_api_route(
    '/v1/transactions',
    create_transaction,
    methods=['POST'],
    tags=['Transaction']
)