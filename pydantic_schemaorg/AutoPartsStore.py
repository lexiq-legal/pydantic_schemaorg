from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness
from pydantic_schemaorg.Store import Store


class AutoPartsStore(AutomotiveBusiness, Store):
    """An auto parts store.

    See https://schema.org/AutoPartsStore.

    """

    locals().update({"@type": Field("AutoPartsStore", const=True)})


AutoPartsStore.update_forward_refs()
