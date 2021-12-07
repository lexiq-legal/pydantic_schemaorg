from pydantic import Field
from pydantic_schemaorg.Store import Store


class OfficeEquipmentStore(Store):
    """An office equipment store.

    See https://schema.org/OfficeEquipmentStore.

    """
    type_: str = Field("OfficeEquipmentStore", const=True, alias='@type')
    

OfficeEquipmentStore.update_forward_refs()
