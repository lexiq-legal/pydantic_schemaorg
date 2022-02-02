from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class PotentialActionStatus(ActionStatusType):
    """A description of an action that is supported.

    See: https://schema.org/PotentialActionStatus
    Model depth: 6
    """
    type_: str = Field("PotentialActionStatus", alias='@type')
    

