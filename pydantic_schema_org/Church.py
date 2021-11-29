from pydantic import Field
from pydantic_schema_org.PlaceOfWorship import PlaceOfWorship


class Church(PlaceOfWorship):
    """A church.

    See https://schema.org/Church.

    """

    locals().update({"@type": Field("Church", const=True)})


Church.update_forward_refs()
