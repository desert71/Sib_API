import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, Request
from envparse import Env
from fastapi.routing import APIRouter, APIRoute
from models import Todo
from random import randint

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/test_database")

app = FastAPI()

async def ping() -> dict:
    return {"Success": True}

async def mainpage() -> dict:
    return {
                "page": "Основная путь API-визитки",
                "owner": "Казеннов Александр Максимович",
                "info": {
                            "education": "Высшее, Московский Авиационный Институт. Специальность - Системный анализ и управление",
                            "work experience": {
                                                    "ноябрь 2022 - март 2023": '''Хохланд Руссланд, стажер системный инжинер.
                                                                                - Разработал сервис аналитики данных из карточек проектов в Kaiten и автоматической 
                                                                                оправки писем по почте ответственным, используя API Kaiten, Python, Pandas.
                                                                                - Подключал сервера, коммутаторы и сетевое оборудование.
                                                                                - Обрабатывал заявки пользователей в ServiceDesk.
                                                                               ''',
                                                    "март 2023 - настоящее время": '''ГБУ 'Миграционный центр', главный специалист по информационной безопасности
                                                                                      - Разработал веб-сайт для проведения тестирования знаний. Стек: Django.
                                                                                      - Участвовал в разработке нормативной документации по информационной безопасности.
                                                                                      - Автоматизировал подготовку ежеквартального анализа данных с помощью Python и Pandas.
                                                                                   ''',
                                                },
                            "about Me": '''Начинающий Python Backend разработчик. 
                                        - Разработал 2 проекта на Python + Django в институте с моделированием движения спутников.
                                        - После прохождения курсов реализовал на этом же стеке проект книжного магазина.
                                        - Также на FastAPI + sklearn + Docker разработал веб-страницу классификации новостного заголовка 
                                        (GitHub: desert71/News_check/tree/master).
                                        ''',
                         },
                "contacts": {
                                "phone": "+7-926-790-81-99 ",
                                "e-mail": "amkazennov99@gmail.com",
                                "Telegram": "A_Deserdzhio",

                            },

            }

async def create_record(request: Request, d: dict) -> dict:
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client["test_database"]
    newRec = Todo(d["title"], d["description"], False)
    newId = randint(1, 10000)
    await mongo_client.records.insert_one({newId: newRec})
    return {"Success": True, "newRecord": newRec}

async def get_record(rrequest: Request, id: int) -> list:
    mongo_client: AsyncIOMotorClient = rrequest.app.state.mongo_client["test_database"]
    cursor = mongo_client.records.find(id)
    res = []
    for document in await cursor.to_list(length=100):
        document["_id"] = str(document["_id"])
        res.append(document)
    return res

routes = [
    APIRoute(path="/ping", endpoint=ping, methods=["GET"]),
    APIRoute(path="/", endpoint=mainpage, methods=["GET"]),
    APIRoute(path="/create_record", endpoint=create_record, methods=["POST"]),
    APIRoute(path="/get_record/{id}", endpoint=get_record, methods=["GET"]),
]
client = AsyncIOMotorClient(MONGODB_URL)
app = FastAPI()
app.state.mongo_client = client
app.include_router(APIRouter(routes=routes))