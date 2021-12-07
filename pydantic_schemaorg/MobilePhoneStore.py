from pydantic import Field
from pydantic_schemaorg.Store import Store


class MobilePhoneStore(Store):
    """A store that sells mobile phones and related accessories.

    See https://schema.org/MobilePhoneStore.

    """
    type_: str = Field("MobilePhoneStore", const=True, alias='@type')
    

MobilePhoneStore.update_forward_refs()
