from invoke import Collection

from .posts import new_post


# Create a collection and add the tasks to it
namespace = Collection()
namespace.add_task(new_post, name="new-post")
