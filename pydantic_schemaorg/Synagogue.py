from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """A synagogue.

    See https://schema.org/Synagogue.

    """

    locals().update({"@type": Field("Synagogue", const=True)})


Synagogue.update_forward_refs()
