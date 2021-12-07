from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class InternetCafe(LocalBusiness):
    """An internet cafe.

    See https://schema.org/InternetCafe.

    """
    type_: str = Field("InternetCafe", const=True, alias='@type')
    

InternetCafe.update_forward_refs()
