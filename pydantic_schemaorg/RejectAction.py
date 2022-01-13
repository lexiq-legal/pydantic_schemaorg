from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AllocateAction import AllocateAction


class RejectAction(AllocateAction):
    """The act of rejecting to/adopting an object. Related actions: * [[AcceptAction]]: The"
     "antonym of RejectAction.

    See: https://schema.org/RejectAction
    Model depth: 5
    """

    type_: str = Field("RejectAction", const=True, alias="@type")


if TYPE_CHECKING:

    RejectAction.update_forward_refs()
