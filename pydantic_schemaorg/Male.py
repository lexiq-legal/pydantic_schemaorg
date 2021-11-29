from pydantic import Field
from pydantic_schemaorg.GenderType import GenderType


class Male(GenderType):
    """The male gender.

    See https://schema.org/Male.

    """

    locals().update({"@type": Field("Male", const=True)})


Male.update_forward_refs()
