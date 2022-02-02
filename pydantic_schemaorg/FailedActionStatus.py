from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class FailedActionStatus(ActionStatusType):
    """An action that failed to complete. The action's error property and the HTTP return code"
     "contain more information about the failure.

    See: https://schema.org/FailedActionStatus
    Model depth: 6
    """
    type_: str = Field("FailedActionStatus", alias='@type')
    

