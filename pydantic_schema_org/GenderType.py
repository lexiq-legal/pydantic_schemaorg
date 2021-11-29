from pydantic import Field
from pydantic_schema_org.Enumeration import Enumeration


class GenderType(Enumeration):
    """An enumeration of genders.

    See https://schema.org/GenderType.

    """

    locals().update({"@type": Field("GenderType", const=True)})


GenderType.update_forward_refs()
