from invoke import Collection

from website.utils.ConfigManager import ConfigManager

from .build import build as build_task
from .install import install as install_task
from .launch_rstudio import launch_rstudio as launch_rstudio_task
from .rosetta import check_rosetta as check_rosetta_task

# Create a collection and add the tasks to it
config_manager = ConfigManager()
config = config_manager.get_config()

namespace = Collection()
namespace.add_task(build_task, name="build")
namespace.add_task(install_task, name="install")
namespace.add_task(launch_rstudio_task, name="launch-rstudio")
namespace.add_task(check_rosetta_task, name="check-rosetta")
