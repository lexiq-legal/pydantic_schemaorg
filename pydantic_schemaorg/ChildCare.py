from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ChildCare(LocalBusiness):
    """A Childcare center.

    See: https://schema.org/ChildCare
    Model depth: 4
    """
    type_: str = Field("ChildCare", alias='@type')
    

