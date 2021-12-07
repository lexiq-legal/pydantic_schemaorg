from pydantic import Field
from pydantic_schemaorg.Action import Action


class OrganizeAction(Action):
    """The act of manipulating/administering/supervising/controlling one or more objects.

    See https://schema.org/OrganizeAction.

    """
    type_: str = Field("OrganizeAction", const=True, alias='@type')
    

OrganizeAction.update_forward_refs()
