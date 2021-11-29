from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """A mosque.

    See https://schema.org/Mosque.

    """

    locals().update({"@type": Field("Mosque", const=True)})


Mosque.update_forward_refs()
