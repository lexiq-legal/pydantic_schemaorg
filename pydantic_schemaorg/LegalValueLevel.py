from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class LegalValueLevel(Enumeration):
    """A list of possible levels for the legal validity of a legislation.

    See https://schema.org/LegalValueLevel.

    """

    locals().update({"@type": Field("LegalValueLevel", const=True)})


LegalValueLevel.update_forward_refs()
