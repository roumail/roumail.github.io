from website.utils.Config import Config


class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            # Initialize the config object here
            cls._instance.config = Config()
        return cls._instance

    def get_config(self) -> Config:
        return self.config
