from pydantic import Field
from pydantic_schemaorg.ContactPointOption import ContactPointOption


class TollFree(ContactPointOption):
    """The associated telephone number is toll free.

    See https://schema.org/TollFree.

    """
    type_: str = Field("TollFree", const=True, alias='@type')
    

TollFree.update_forward_refs()
