from pydantic import Field
from pydantic_schemaorg.Action import Action


class OrganizeAction(Action):
    """The act of manipulating/administering/supervising/controlling one or more objects.

    See https://schema.org/OrganizeAction.

    """

    locals().update({"@type": Field("OrganizeAction", const=True)})


OrganizeAction.update_forward_refs()
