from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class RejectAction(AllocateAction):
    """The act of rejecting to/adopting an object. Related actions: * [[AcceptAction]]: The"
     "antonym of RejectAction.

    See https://schema.org/RejectAction.

    """

    locals().update({"@type": Field("RejectAction", const=True)})


RejectAction.update_forward_refs()
