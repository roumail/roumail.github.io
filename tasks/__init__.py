from invoke import Collection

from .build import build as build_task
from .install import install as install_task
from .launch_rstudio import launch_rstudio as launch_rstudio_task
from .posts import new_post
from .rosetta import check_rosetta as check_rosetta_task

# Create a collection and add the tasks to it
namespace = Collection()
namespace.add_task(build_task, name="build")
namespace.add_task(install_task, name="install")
namespace.add_task(launch_rstudio_task, name="launch-rstudio")
namespace.add_task(check_rosetta_task, name="check-rosetta")
namespace.add_task(new_post, name="new-post")
