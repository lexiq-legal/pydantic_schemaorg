from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class SelfStorage(LocalBusiness):
    """A self-storage facility.

    See: https://schema.org/SelfStorage
    Model depth: 4
    """
    type_: str = Field("SelfStorage", alias='@type')
    

