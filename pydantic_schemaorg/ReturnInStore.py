from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnInStore(ReturnMethodEnumeration):
    """Specifies that product returns must be made in a store.

    See: https://schema.org/ReturnInStore
    Model depth: 5
    """

    type_: str = Field("ReturnInStore", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnInStore.update_forward_refs()
