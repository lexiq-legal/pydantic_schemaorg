from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class InternetCafe(LocalBusiness):
    """An internet cafe.

    See: https://schema.org/InternetCafe
    Model depth: 4
    """
    type_: str = Field("InternetCafe", alias='@type')
    

