from jinja2 import Template
import yaml
import re


def read_config():
    with open("config.yaml.j2", "r") as file:
        content = file.read()

    # Extract the fixed values using regular expressions
    project_root_dir = re.search(r"project_root_dir:\s*(.+)", content).group(1)
    project_dir_container = re.search(r"project_dir_container:\s*(.+)", content).group(
        1
    )
    home_dir_container = re.search(r"home_dir_container:\s*(.+)", content).group(1)

    # Render the template using the extracted values
    template = Template(content)
    config_yaml = template.render(
        project_root_dir=project_root_dir,
        project_dir_container=project_dir_container,
        home_dir_container=home_dir_container,
    )

    return yaml.safe_load(config_yaml)


def create_volume_mounts(volume_mounts):
    return [f"-v {mount['local']}:{mount['container']}" for mount in volume_mounts]
