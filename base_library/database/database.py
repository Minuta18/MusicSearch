import sqlalchemy
import typing
from sqlalchemy import ext
from sqlalchemy import orm

def init_connection(database_url: str) -> tuple[typing.Any, typing.Any]:
    engine = ext.asyncio.create_async_engine(database_url)
    session = orm.sessionmaker(
        bind=engine,
        class_=ext.asyncio.AsyncSession,
        expire_on_commit=False,
    )
    
    return engine, session

async def destroy_connection(engine: ext.asyncio.AsyncEngine) -> None:
    engine.dispose()

async def init_models(
    engine: ext.asyncio.AsyncEngine, 
    base: ext.declarative
) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

async def destroy_models(
    engine: ext.asyncio.AsyncEngine, base: ext.declarative
) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.drop_all)


