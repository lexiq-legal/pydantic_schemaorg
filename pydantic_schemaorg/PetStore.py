from pydantic import Field
from pydantic_schemaorg.Store import Store


class PetStore(Store):
    """A pet store.

    See https://schema.org/PetStore.

    """

    locals().update({"@type": Field("PetStore", const=True)})


PetStore.update_forward_refs()
