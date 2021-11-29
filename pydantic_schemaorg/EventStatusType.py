from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class EventStatusType(StatusEnumeration):
    """EventStatusType is an enumeration type whose instances represent several states that"
     "an Event may be in.

    See https://schema.org/EventStatusType.

    """

    locals().update({"@type": Field("EventStatusType", const=True)})


EventStatusType.update_forward_refs()
