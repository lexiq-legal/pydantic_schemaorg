from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class OfficeEquipmentStore(Store):
    """An office equipment store.

    See: https://schema.org/OfficeEquipmentStore
    Model depth: 5
    """

    type_: str = Field("OfficeEquipmentStore", const=True, alias="@type")


if TYPE_CHECKING:

    OfficeEquipmentStore.update_forward_refs()
