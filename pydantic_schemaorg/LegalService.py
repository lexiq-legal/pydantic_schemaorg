from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class LegalService(LocalBusiness):
    """A LegalService is a business that provides legally-oriented services, advice and representation,"
     "e.g. law firms. As a [[LocalBusiness]] it can be described as a [[provider]] of one or"
     "more [[Service]]\(s).

    See: https://schema.org/LegalService
    Model depth: 4
    """
    type_: str = Field("LegalService", alias='@type')
    

