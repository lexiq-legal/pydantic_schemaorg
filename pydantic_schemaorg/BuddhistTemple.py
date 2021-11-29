from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """A Buddhist temple.

    See https://schema.org/BuddhistTemple.

    """

    locals().update({"@type": Field("BuddhistTemple", const=True)})


BuddhistTemple.update_forward_refs()
