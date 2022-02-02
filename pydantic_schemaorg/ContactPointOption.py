from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ContactPointOption(Enumeration):
    """Enumerated options related to a ContactPoint.

    See: https://schema.org/ContactPointOption
    Model depth: 4
    """
    type_: str = Field("ContactPointOption", alias='@type')
    

