from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class ShortStory(CreativeWork):
    """Short story or tale. A brief work of literature, usually written in narrative prose.

    See https://schema.org/ShortStory.

    """

    locals().update({"@type": Field("ShortStory", const=True)})


ShortStory.update_forward_refs()
