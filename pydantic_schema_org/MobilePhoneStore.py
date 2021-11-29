from pydantic import Field
from pydantic_schema_org.Store import Store


class MobilePhoneStore(Store):
    """A store that sells mobile phones and related accessories.

    See https://schema.org/MobilePhoneStore.

    """

    locals().update({"@type": Field("MobilePhoneStore", const=True)})


MobilePhoneStore.update_forward_refs()
