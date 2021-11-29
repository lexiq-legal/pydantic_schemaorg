from pydantic import Field
from pydantic_schema_org.ContactPointOption import ContactPointOption


class HearingImpairedSupported(ContactPointOption):
    """Uses devices to support users with hearing impairments.

    See https://schema.org/HearingImpairedSupported.

    """

    locals().update({"@type": Field("HearingImpairedSupported", const=True)})


HearingImpairedSupported.update_forward_refs()
