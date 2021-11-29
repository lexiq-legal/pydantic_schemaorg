from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Sculpture(CreativeWork):
    """A piece of sculpture.

    See https://schema.org/Sculpture.

    """

    locals().update({"@type": Field("Sculpture", const=True)})


Sculpture.update_forward_refs()
