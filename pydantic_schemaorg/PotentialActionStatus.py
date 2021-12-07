from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class PotentialActionStatus(ActionStatusType):
    """A description of an action that is supported.

    See https://schema.org/PotentialActionStatus.

    """
    type_: str = Field("PotentialActionStatus", const=True, alias='@type')
    

PotentialActionStatus.update_forward_refs()
