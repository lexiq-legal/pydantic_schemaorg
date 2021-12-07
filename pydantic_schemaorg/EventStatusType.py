from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class EventStatusType(StatusEnumeration):
    """EventStatusType is an enumeration type whose instances represent several states that"
     "an Event may be in.

    See https://schema.org/EventStatusType.

    """
    type_: str = Field("EventStatusType", const=True, alias='@type')
    

EventStatusType.update_forward_refs()
