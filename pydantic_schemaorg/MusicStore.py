from pydantic import Field
from pydantic_schemaorg.Store import Store


class MusicStore(Store):
    """A music store.

    See https://schema.org/MusicStore.

    """

    locals().update({"@type": Field("MusicStore", const=True)})


MusicStore.update_forward_refs()
