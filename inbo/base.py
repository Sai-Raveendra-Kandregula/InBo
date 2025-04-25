from contextlib import asynccontextmanager
from typing import Optional
import aiohttp
from fastapi import FastAPI, Request
import uvicorn
import logging

from .events import GLWebhookMREventData
from .events.mr import MRAction

from enum import Enum

DEF_PORT=11235

class GLWebHookType(Enum):
    """GL Webhook event type"""
    MERGE_REQUEST = "merge_request"
    UNKNOWN = "unknown"
    

class GLWebhookEvent:
    def __init__(self, **kwargs):
        self.raw = kwargs
        self.type = GLWebHookType.UNKNOWN
        
        if "event_type" in kwargs and kwargs["event_type"] == "merge_request":
            self.type = GLWebHookType.MERGE_REQUEST
    
    @property
    def data(self):
        if self.type == GLWebHookType.MERGE_REQUEST:
            return GLWebhookMREventData(**self.raw)
        return self.raw
    
    def json(self):
        return self.raw

class Inbo():
    def __init__(self, name : Optional[str] = "GL Bot", secret : Optional[str] = None, access_token : Optional[str] = None, debug : Optional[bool] = False):
        self.name = name
        self.__wh_secret = secret
        self.__access_token = access_token
        self.__fastapi_app = self.__create_app()
        logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s')
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        if debug:
            self.logger.setLevel(logging.DEBUG)
    
    async def merge_request_event(self, gl, action : MRAction, data : GLWebhookMREventData):
        self.logger.info(f"Recieved MR {action} Event :")
        self.logger.info(data)
        
    def get_fastapi_app(self):
        return self.__fastapi_app
    
    def __create_app(self):
        @asynccontextmanager
        async def lifecycle(app : FastAPI):
            self.logger.info("I am On.")
            yield
            self.logger.info("Bye bye!")
        
        app = FastAPI(title=self.name, lifespan=lifecycle)
        
        @app.post("/")
        async def handle_webhook_event(request: Request):
            gl_ins = request.headers["x-gitlab-instance"]
            ev_raw = await request.json()
            ev = GLWebhookEvent(**ev_raw)
            self.logger.debug(f"Event : {ev.type}")
            self.logger.debug(ev.data)
            gl_sess_headers = {}
            if self.__access_token is not None:
                gl_sess_headers["PRIVATE-TOKEN"] = self.__access_token
            async with aiohttp.client.ClientSession(
                base_url=gl_ins,
                headers=gl_sess_headers
            ) as gl:
                if ev.type == GLWebHookType.MERGE_REQUEST:
                    await self.merge_request_event(gl, ev.data['object_attributes']['action'], ev.data)
            return {}
        return app

    def run(self, host : Optional[str] = "0.0.0.0", port : Optional[int] = DEF_PORT, *args, **kwargs):
        uvicorn.run(app=self.__fastapi_app, host=host, port=port, log_level=logging.CRITICAL, *args, **kwargs)