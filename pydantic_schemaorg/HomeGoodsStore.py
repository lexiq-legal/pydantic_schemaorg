from pydantic import Field
from pydantic_schemaorg.Store import Store


class HomeGoodsStore(Store):
    """A home goods store.

    See https://schema.org/HomeGoodsStore.

    """

    locals().update({"@type": Field("HomeGoodsStore", const=True)})


HomeGoodsStore.update_forward_refs()
