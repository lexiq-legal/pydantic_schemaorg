from pydantic import Field
from pydantic_schemaorg.OrganizeAction import OrganizeAction


class AllocateAction(OrganizeAction):
    """The act of organizing tasks/objects/events by associating resources to it.

    See https://schema.org/AllocateAction.

    """

    locals().update({"@type": Field("AllocateAction", const=True)})


AllocateAction.update_forward_refs()
