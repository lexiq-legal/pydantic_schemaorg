from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ContactPointOption(Enumeration):
    """Enumerated options related to a ContactPoint.

    See https://schema.org/ContactPointOption.

    """

    locals().update({"@type": Field("ContactPointOption", const=True)})


ContactPointOption.update_forward_refs()
