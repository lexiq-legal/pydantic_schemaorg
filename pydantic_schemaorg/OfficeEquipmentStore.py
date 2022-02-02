from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class OfficeEquipmentStore(Store):
    """An office equipment store.

    See: https://schema.org/OfficeEquipmentStore
    Model depth: 5
    """
    type_: str = Field("OfficeEquipmentStore", alias='@type')
    

