from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class HomeAndConstructionBusiness(LocalBusiness):
    """A construction business. A HomeAndConstructionBusiness is a [[LocalBusiness]] that"
     "provides services around homes and buildings. As a [[LocalBusiness]] it can be described"
     "as a [[provider]] of one or more [[Service]]\(s).

    See: https://schema.org/HomeAndConstructionBusiness
    Model depth: 4
    """
    type_: str = Field("HomeAndConstructionBusiness", alias='@type')
    

