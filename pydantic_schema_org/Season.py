from pydantic import Field
from pydantic_schema_org.CreativeWork import CreativeWork


class Season(CreativeWork):
    """A media season e.g. tv, radio, video game etc.

    See https://schema.org/Season.

    """

    locals().update({"@type": Field("Season", const=True)})


Season.update_forward_refs()
