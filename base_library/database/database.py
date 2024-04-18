import sqlalchemy
import typing
from sqlalchemy.ext import asyncio
from sqlalchemy import orm

def init_connection(database_url: str) -> tuple[typing.Any, typing.Any]:
    engine = asyncio.create_async_engine(database_url)
    session = orm.sessionmaker(
        bind=engine,
        class_=asyncio.AsyncSession,
        expire_on_commit=False,
    )
    
    return engine, session

async def destroy_connection(engine: asyncio.AsyncEngine) -> None:
    engine.dispose()

async def init_models(
    engine: asyncio.AsyncEngine, 
    base: orm.decl_api.DeclarativeMeta
) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

async def destroy_models(
    engine: asyncio.AsyncEngine, base: orm.decl_api.DeclarativeMeta
) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.drop_all)


