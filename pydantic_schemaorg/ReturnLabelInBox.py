from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelInBox(ReturnLabelSourceEnumeration):
    """Specifies that a return label will be provided by the seller in the shipping box.

    See: https://schema.org/ReturnLabelInBox
    Model depth: 5
    """

    type_: str = Field("ReturnLabelInBox", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnLabelInBox.update_forward_refs()
