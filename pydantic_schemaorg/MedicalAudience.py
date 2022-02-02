from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PeopleAudience import PeopleAudience
from pydantic_schemaorg.Audience import Audience


class MedicalAudience(PeopleAudience, Audience):
    """Target audiences for medical web pages.

    See: https://schema.org/MedicalAudience
    Model depth: 4
    """
    type_: str = Field("MedicalAudience", alias='@type')
    

