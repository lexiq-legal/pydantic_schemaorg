from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class CompletedActionStatus(ActionStatusType):
    """An action that has already taken place.

    See: https://schema.org/CompletedActionStatus
    Model depth: 6
    """
    type_: str = Field("CompletedActionStatus", alias='@type')
    

