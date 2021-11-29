from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Volcano(Landform):
    """A volcano, like Fuji san.

    See https://schema.org/Volcano.

    """

    locals().update({"@type": Field("Volcano", const=True)})


Volcano.update_forward_refs()
