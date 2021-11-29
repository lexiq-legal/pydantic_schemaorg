from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class AssignAction(AllocateAction):
    """The act of allocating an action/event/task to some destination (someone or something).

    See https://schema.org/AssignAction.

    """

    locals().update({"@type": Field("AssignAction", const=True)})


AssignAction.update_forward_refs()
