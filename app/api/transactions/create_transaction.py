import fastapi


from fastapi import Header


async def create_transaction(user_id: int = Header(0, alias='X-Consumer-ID')):
    pass
