from pydantic import Field
from pydantic_schema_org.Store import Store


class JewelryStore(Store):
    """A jewelry store.

    See https://schema.org/JewelryStore.

    """

    locals().update({"@type": Field("JewelryStore", const=True)})


JewelryStore.update_forward_refs()
