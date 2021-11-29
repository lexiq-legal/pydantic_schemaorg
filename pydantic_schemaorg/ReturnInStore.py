from pydantic import Field
from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnInStore(ReturnMethodEnumeration):
    """Specifies that product returns must be made in a store.

    See https://schema.org/ReturnInStore.

    """

    locals().update({"@type": Field("ReturnInStore", const=True)})


ReturnInStore.update_forward_refs()
