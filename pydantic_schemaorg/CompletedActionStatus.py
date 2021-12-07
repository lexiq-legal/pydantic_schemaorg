from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class CompletedActionStatus(ActionStatusType):
    """An action that has already taken place.

    See https://schema.org/CompletedActionStatus.

    """
    type_: str = Field("CompletedActionStatus", const=True, alias='@type')
    

CompletedActionStatus.update_forward_refs()
