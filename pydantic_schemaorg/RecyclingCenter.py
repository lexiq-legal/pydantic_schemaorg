from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """A recycling center.

    See https://schema.org/RecyclingCenter.

    """
    type_: str = Field("RecyclingCenter", const=True, alias='@type')
    

RecyclingCenter.update_forward_refs()
