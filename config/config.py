import logging
import json


class Config:
    _instance = None
    config: dict = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logger = lambda msg: print(msg)
            try:
                with open('./config/.config.json') as file:
                    cls._instance.config = json.load(file)
            except Exception as e:
                cls._instance.logger.info(
                    f"!!! Failed to load config: {e} !!!")
                cls._instance.config = {}

        return cls._instance

    def get_config_item(self, name: str, default=None):
        return self.config.get(name, default)
