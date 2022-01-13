from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InformAction import InformAction


class ConfirmAction(InformAction):
    """The act of notifying someone that a future event/action is going to happen as expected."
     "Related actions: * [[CancelAction]]: The antonym of ConfirmAction.

    See: https://schema.org/ConfirmAction
    Model depth: 6
    """

    type_: str = Field("ConfirmAction", const=True, alias="@type")


if TYPE_CHECKING:

    ConfirmAction.update_forward_refs()
