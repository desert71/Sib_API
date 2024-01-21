from fastapi import FastAPI
from fastapi.routing import APIRouter, APIRoute

app = FastAPI()

async def ping() -> dict:
    return {"Success": True}

async def mainpage() -> str:
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

routes = [
    APIRoute(path="/ping", endpoint=ping, methods=["GET"]),
    APIRoute(path="/", endpoint=mainpage, methods=["GET"], response_model=dict),
]

app.include_router(APIRouter(routes=routes))