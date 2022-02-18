from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ContactPointOption import ContactPointOption


class TollFree(ContactPointOption):
    """The associated telephone number is toll free.

    See: https://schema.org/TollFree
    Model depth: 5
    """
    type_: str = Field(default="TollFree", alias='@type', const=True)
    
