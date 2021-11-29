from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Painting(CreativeWork):
    """A painting.

    See https://schema.org/Painting.

    """

    locals().update({"@type": Field("Painting", const=True)})


Painting.update_forward_refs()
