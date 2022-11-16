from time import sleep

import requests
import uvicorn
from fastapi import FastAPI

from pong.data_models import Response


def create_app() -> FastAPI:
    """
    Function to create FastAPI instance.

    :return: FastAPI object
    """
    return FastAPI()


instance_2 = create_app()


@instance_2.get("/ping")
async def ping(pong_time_ms: float) -> Response:
    """
    Function to create a 'ping' call.

    :param pong_time_ms: time in milliseconds to send the 'pong' request after
    :return: response from request
    """
    # Divide in 0.01 to convert time to milliseconds
    sleep(pong_time_ms / 0.01)

    # Create response body
    post_body = Response(action="pong (from server 2 to server 1)")

    response = requests.post("localhost:8000/ping", post_body)
    return response


if __name__ == "__main__":
    uvicorn.run(instance_2, host="0.0.0.0", port=8001)
