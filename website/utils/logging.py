import logging
import logging.config
import os

import importlib_resources
import yaml


def get_logger(module_name):
    parts = module_name.split(".")

    # Use only the last part (the actual module name) as the logger name
    logger_name = parts[-1]

    logger = logging.getLogger(logger_name)

    # Check if logging has been initialized
    if not logging.getLogger().hasHandlers():
        initialize_logging()

    return logger


def initialize_logging(
    log_dir="var/log",
):
    # Get the base directory from an environment variable
    if not os.path.exists(log_dir):
        print(f"specified log_directory doesn't exist: {log_dir}. Creating directory..")
        os.makedirs(log_dir, exist_ok=True)

    # Use the default path to the config file
    path2log_config = importlib_resources.files("tasks").joinpath("etc/logging.yml")

    # Load the logging configuration file
    with open(path2log_config) as f:
        config = yaml.safe_load(f)

    # Replace the {LOG_DIR} placeholder with the actual base directory
    for _, handler in config["handlers"].items():
        if "filename" in handler:
            log_directory = handler["filename"].format(LOG_DIR=log_dir)
            handler["filename"] = log_directory

    logging.config.dictConfig(config)

    return log_dir


class LoggerFile:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        for line in message.rstrip().splitlines():
            self.logger.log(self.level, line.rstrip())

    def flush(self):
        pass
