from pydantic import Field
from pydantic_schema_org.Store import Store


class OfficeEquipmentStore(Store):
    """An office equipment store.

    See https://schema.org/OfficeEquipmentStore.

    """

    locals().update({"@type": Field("OfficeEquipmentStore", const=True)})


OfficeEquipmentStore.update_forward_refs()
