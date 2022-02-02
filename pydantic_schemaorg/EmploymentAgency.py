from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """An employment agency.

    See: https://schema.org/EmploymentAgency
    Model depth: 4
    """
    type_: str = Field("EmploymentAgency", alias='@type')
    

