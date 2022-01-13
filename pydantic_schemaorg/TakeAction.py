from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.TransferAction import TransferAction


class TakeAction(TransferAction):
    """The act of gaining ownership of an object from an origin. Reciprocal of GiveAction. Related"
     "actions: * [[GiveAction]]: The reciprocal of TakeAction. * [[ReceiveAction]]: Unlike"
     "ReceiveAction, TakeAction implies that ownership has been transfered.

    See: https://schema.org/TakeAction
    Model depth: 4
    """

    type_: str = Field("TakeAction", const=True, alias="@type")


if TYPE_CHECKING:

    TakeAction.update_forward_refs()
