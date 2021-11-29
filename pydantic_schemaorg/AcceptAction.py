from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class AcceptAction(AllocateAction):
    """The act of committing to/adopting an object. Related actions: * [[RejectAction]]:"
     "The antonym of AcceptAction.

    See https://schema.org/AcceptAction.

    """

    locals().update({"@type": Field("AcceptAction", const=True)})


AcceptAction.update_forward_refs()
