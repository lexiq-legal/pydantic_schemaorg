from pydantic import Field
from pydantic_schema_org.AutomotiveBusiness import AutomotiveBusiness
from pydantic_schema_org.Store import Store


class AutoPartsStore(AutomotiveBusiness, Store):
    """An auto parts store.

    See https://schema.org/AutoPartsStore.

    """

    locals().update({"@type": Field("AutoPartsStore", const=True)})


AutoPartsStore.update_forward_refs()
