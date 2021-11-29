from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """A Hindu temple.

    See https://schema.org/HinduTemple.

    """

    locals().update({"@type": Field("HinduTemple", const=True)})


HinduTemple.update_forward_refs()
