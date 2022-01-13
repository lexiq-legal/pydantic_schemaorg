from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnAtKiosk(ReturnMethodEnumeration):
    """Specifies that product returns must be made at a kiosk.

    See: https://schema.org/ReturnAtKiosk
    Model depth: 5
    """

    type_: str = Field("ReturnAtKiosk", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnAtKiosk.update_forward_refs()
