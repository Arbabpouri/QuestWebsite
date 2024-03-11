from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel
from pydantic import ValidationError
from typing import List, Union
from modules.response import Response
from modules.database import Database, QuestsAndAnswers
from modules.enums import ResponseCode, ResponseMessage



app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# region models

class AnsewrModel(BaseModel):
    id: int
    answer: Union[str, int]


class AnsewrsModel(BaseModel):
    answers: List[AnsewrModel]


class AnswersResponse(BaseModel):
    quest_1: str
    quest_2: int
    quest_3: int
    quest_4: str
    quest_5: str
    quest_6: int
    quest_7: int
    quest_8: str
    quest_9: int
    quest_10: int
    quest_11: int
    quest_12: str


class AnswersListResponse(BaseModel):
    answers: List[AnswersResponse]
# endregion


database = Database()


# region routers
@app.post("/get-answer")
async def get_answers(answers: AnsewrsModel) -> Response:

    try:

        answers: List[AnsewrModel] = answers.answers

        if len(answers) != 12:

            response = Response(
                status=ResponseCode.BAD_DATA,
                message=ResponseMessage.BAD_DATA
            )

        else:

            answers = sorted(answers, key=lambda item: item.id)

            validation = AnswersResponse(
                quest_1=answers[0].answer,
                quest_2=answers[1].answer,
                quest_3=answers[2].answer,
                quest_4=answers[3].answer,
                quest_5=answers[4].answer,
                quest_6=answers[5].answer,
                quest_7=answers[6].answer,
                quest_8=answers[7].answer,
                quest_9=answers[8].answer,
                quest_10=answers[9].answer,
                quest_11=answers[10].answer,
                quest_12=answers[11].answer,
            )

            answer = QuestsAndAnswers(
                quest_1=validation.quest_1,
                quest_2=validation.quest_2,
                quest_3=validation.quest_3,
                quest_4=validation.quest_4,
                quest_5=validation.quest_5,
                quest_6=validation.quest_6,
                quest_7=validation.quest_7,
                quest_8=validation.quest_8,
                quest_9=validation.quest_9,
                quest_10=validation.quest_10,
                quest_11=validation.quest_11,
                quest_12=validation.quest_12,
            )

            database.session.add(answer)
            database.session.commit()

            response = Response(
                status=ResponseCode.OK,
                message=ResponseMessage.OK
            )

    except ValidationError:
     
        response = Response(
            status=ResponseCode.BAD_DATA,
            message=ResponseMessage.BAD_DATA
        )

    except Exception:

        response = Response(
            status=ResponseCode.ERROR,
            message=ResponseMessage.ERROR
        )

    finally:

        return JSONResponse(response.dict())


@app.get("/show-answer")
async def show_answer(token: str) -> Response:

    try:

        ــTOKEN__ = "5f5c92f0-3a37-41c6-b96d-c83554311245"

        if token == ــTOKEN__:

            data = database.session.query(QuestsAndAnswers).all()

            answers_list = list()

            for answers in data:

                answer_obj = AnswersResponse(
                    quest_1=answers.quest_1,
                    quest_2=answers.quest_2,
                    quest_3=answers.quest_3,
                    quest_4=answers.quest_4,
                    quest_5=answers.quest_5,
                    quest_6=answers.quest_6,
                    quest_7=answers.quest_7,
                    quest_8=answers.quest_8,
                    quest_9=answers.quest_9,
                    quest_10=answers.quest_10,
                    quest_11=answers.quest_11,
                    quest_12=answers.quest_12,
                )

                answers_list.append(answer_obj)

            answers_list = AnswersListResponse(answers=answers_list)
            answers_list = answers_list.dict()

            response = Response(
                status=ResponseCode.OK,
                message=ResponseMessage.OK, result=answers_list
            )

        else:

            response = Response(
                status=ResponseCode.INVALIED_TOKEN,
                message=ResponseMessage.INVALIED_TOKEN
            )

    except Exception as error:

        response = Response(
            status=ResponseCode.ERROR,
            message=ResponseMessage.ERROR
        )

    finally:

        return JSONResponse(response.dict())


# endregion


if __name__ == "__main__":
    uvicorn.run("main_fastapi:app", host="127.0.0.1", port=5000, log_level="info")
