import importlib
import os
from glob import glob

from bot import dp
from utils.db import Base, engine


async def import_module(module_name) -> list:
    files = glob(os.path.join(module_name, '**/*.py'))
    response = []
    for file in files:
        file = file[:-3]
        module = importlib.import_module(file.replace("/", "."))
        response.append(module)
    return response


async def import_handlers():
    modules = await import_module("handlers")
    for module in modules:
        if hasattr(module, "router"):
            dp.include_router(module.router)


async def import_db():
    Base.metadata.create_all(engine)
