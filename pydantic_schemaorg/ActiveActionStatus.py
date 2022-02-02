from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class ActiveActionStatus(ActionStatusType):
    """An in-progress action (e.g, while watching the movie, or driving to a location).

    See: https://schema.org/ActiveActionStatus
    Model depth: 6
    """
    type_: str = Field("ActiveActionStatus", alias='@type')
    

