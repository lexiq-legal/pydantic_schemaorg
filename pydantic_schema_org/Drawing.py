from pydantic import Field
from pydantic_schema_org.CreativeWork import CreativeWork


class Drawing(CreativeWork):
    """A picture or diagram made with a pencil, pen, or crayon rather than paint.

    See https://schema.org/Drawing.

    """

    locals().update({"@type": Field("Drawing", const=True)})


Drawing.update_forward_refs()
