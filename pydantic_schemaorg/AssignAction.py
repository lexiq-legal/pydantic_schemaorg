from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class AssignAction(AllocateAction):
    """The act of allocating an action/event/task to some destination (someone or something).

    See: https://schema.org/AssignAction
    Model depth: 5
    """
    type_: str = Field("AssignAction", alias='@type')
    

