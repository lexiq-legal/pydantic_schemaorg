from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ContactPointOption(Enumeration):
    """Enumerated options related to a ContactPoint.

    See https://schema.org/ContactPointOption.

    """
    type_: str = Field("ContactPointOption", const=True, alias='@type')
    

ContactPointOption.update_forward_refs()
