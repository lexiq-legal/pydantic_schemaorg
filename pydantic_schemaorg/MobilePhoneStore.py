from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class MobilePhoneStore(Store):
    """A store that sells mobile phones and related accessories.

    See: https://schema.org/MobilePhoneStore
    Model depth: 5
    """

    type_: str = Field("MobilePhoneStore", const=True, alias="@type")


if TYPE_CHECKING:

    MobilePhoneStore.update_forward_refs()
