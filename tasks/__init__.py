from invoke import Collection

from .posts import new_post, list_draft_posts
from .release import tag_version

# Create a collection and add the tasks to it
namespace = Collection()
namespace.add_task(new_post, name="new-post")
namespace.add_task(list_draft_posts, name="list-draft-posts")
namespace.add_task(tag_version, name="push-package-release")
