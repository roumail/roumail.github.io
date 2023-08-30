import importlib.resources
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from jinja2 import Template

from website.etc.constants import (
    HOME_DIR_CONTAINER,
    IMAGE_TAG,
    PACKAGE_NAME,
    PROJECT_DIR_CONTAINER,
)


class ConfigError(Exception):
    pass


class Config:
    def __init__(self):
        # This value may not equal project_root_dir when executed in a container
        entrypoint_exe_dir = Path(os.getcwd())
        self.entrypoint_exe_dir = entrypoint_exe_dir
        env_path = entrypoint_exe_dir / ".env"
        if not env_path.exists():
            self.copy_env_example_file(env_path)
            raise ConfigError(".env not found project root directory")
        else:
            self.load_env_vars(env_path)
        # read config
        self.config_dict = self.read_config()

    def get(self, key, default=None):
        if key not in self.config_dict:
            raise KeyError(f"Configuration key '{key}' not found.")
        return self.config_dict.get(key, default)

    def copy_env_example_file(self, user_env_path):
        # Path to the user's .env file
        user_env_path = Path(user_env_path)

        # Check if the .env file already exists
        if not user_env_path.exists():
            print("Didn't find .env in project root")
            print("Copying example .env that is read by script for database checks")
            print("Please ensure to update parameters `ADMIN_USER` and `DB_USER`")
            # Open the example .env file packaged with the application
            with importlib.resources.open_text(
                f"{PACKAGE_NAME}.etc", ".env.example"
            ) as example_file:
                # Copy the content to the user's directory
                with open(user_env_path, "w") as user_file:
                    user_file.write(example_file.read())

    def load_env_vars(self, env_path):
        load_dotenv(dotenv_path=env_path)
        project_root = os.getenv("BASE_DIR")
        if project_root == "enter/path/here":
            raise ConfigError(
                "Please update `BASE_DIR` value to point to project directory"
            )
        self.project_root = project_root

    def read_config(self):
        # get
        DEFAULT_CONFIG_PATH = importlib.resources.files(PACKAGE_NAME).joinpath(
            "etc/config.yaml.j2"
        )
        with open(DEFAULT_CONFIG_PATH, "r") as file:
            content = file.read()

        # Render the template using the extracted values
        template = Template(content)
        config_yaml = template.render(
            project_root_dir=self.project_root,
            project_dir_container=PROJECT_DIR_CONTAINER,
            home_dir_container=HOME_DIR_CONTAINER,
            image_tag=IMAGE_TAG,
        )

        return yaml.safe_load(config_yaml)


# def read_config():
#     DEFAULT_CONFIG_PATH = importlib.resources.files(PACKAGE_NAME).joinpath(
#         "etc/config.yaml.j2"
#     )
#     with open(DEFAULT_CONFIG_PATH, "r") as file:
#         content = file.read()


#     # Render the template using the extracted values
#     template = Template(content)
#     config_yaml = template.render(
#         project_root_dir=project_root_dir,
#         project_dir_container=PROJECT_DIR_CONTAINER,
#         home_dir_container=HOME_DIR_CONTAINER,
#     )

#     return yaml.safe_load(config_yaml)
