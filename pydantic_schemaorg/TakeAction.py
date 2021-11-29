from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class TakeAction(TransferAction):
    """The act of gaining ownership of an object from an origin. Reciprocal of GiveAction. Related"
     "actions: * [[GiveAction]]: The reciprocal of TakeAction. * [[ReceiveAction]]: Unlike"
     "ReceiveAction, TakeAction implies that ownership has been transfered.

    See https://schema.org/TakeAction.

    """

    locals().update({"@type": Field("TakeAction", const=True)})


TakeAction.update_forward_refs()
