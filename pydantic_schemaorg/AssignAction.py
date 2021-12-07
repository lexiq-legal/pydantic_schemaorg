from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class AssignAction(AllocateAction):
    """The act of allocating an action/event/task to some destination (someone or something).

    See https://schema.org/AssignAction.

    """
    type_: str = Field("AssignAction", const=True, alias='@type')
    

AssignAction.update_forward_refs()
