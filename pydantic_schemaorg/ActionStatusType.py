from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class ActionStatusType(StatusEnumeration):
    """The status of an Action.

    See: https://schema.org/ActionStatusType
    Model depth: 5
    """
    type_: str = Field("ActionStatusType", alias='@type')
    

