from pydantic import Field
from pydantic_schemaorg.Store import Store


class ConvenienceStore(Store):
    """A convenience store.

    See https://schema.org/ConvenienceStore.

    """

    locals().update({"@type": Field("ConvenienceStore", const=True)})


ConvenienceStore.update_forward_refs()
