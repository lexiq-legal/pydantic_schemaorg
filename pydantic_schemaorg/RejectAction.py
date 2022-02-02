from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class RejectAction(AllocateAction):
    """The act of rejecting to/adopting an object. Related actions: * [[AcceptAction]]: The"
     "antonym of RejectAction.

    See: https://schema.org/RejectAction
    Model depth: 5
    """
    type_: str = Field("RejectAction", alias='@type')
    

