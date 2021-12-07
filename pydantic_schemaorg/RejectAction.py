from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class RejectAction(AllocateAction):
    """The act of rejecting to/adopting an object. Related actions: * [[AcceptAction]]: The"
     "antonym of RejectAction.

    See https://schema.org/RejectAction.

    """
    type_: str = Field("RejectAction", const=True, alias='@type')
    

RejectAction.update_forward_refs()
