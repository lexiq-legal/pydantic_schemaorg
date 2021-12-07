from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class SelfStorage(LocalBusiness):
    """A self-storage facility.

    See https://schema.org/SelfStorage.

    """
    type_: str = Field("SelfStorage", const=True, alias='@type')
    

SelfStorage.update_forward_refs()
