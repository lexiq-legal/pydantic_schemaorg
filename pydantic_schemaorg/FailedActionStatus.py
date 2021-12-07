from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class FailedActionStatus(ActionStatusType):
    """An action that failed to complete. The action's error property and the HTTP return code"
     "contain more information about the failure.

    See https://schema.org/FailedActionStatus.

    """
    type_: str = Field("FailedActionStatus", const=True, alias='@type')
    

FailedActionStatus.update_forward_refs()
