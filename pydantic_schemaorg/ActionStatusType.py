from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class ActionStatusType(StatusEnumeration):
    """The status of an Action.

    See https://schema.org/ActionStatusType.

    """
    type_: str = Field("ActionStatusType", const=True, alias='@type')
    

ActionStatusType.update_forward_refs()
