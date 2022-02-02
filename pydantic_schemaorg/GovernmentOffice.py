from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class GovernmentOffice(LocalBusiness):
    """A government office&#x2014;for example, an IRS or DMV office.

    See: https://schema.org/GovernmentOffice
    Model depth: 4
    """
    type_: str = Field("GovernmentOffice", alias='@type')
    

