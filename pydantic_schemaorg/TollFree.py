from pydantic import Field
from pydantic_schemaorg.ContactPointOption import ContactPointOption


class TollFree(ContactPointOption):
    """The associated telephone number is toll free.

    See https://schema.org/TollFree.

    """

    locals().update({"@type": Field("TollFree", const=True)})


TollFree.update_forward_refs()
