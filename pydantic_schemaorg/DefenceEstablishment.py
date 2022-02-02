from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """A defence establishment, such as an army or navy base.

    See: https://schema.org/DefenceEstablishment
    Model depth: 5
    """
    type_: str = Field("DefenceEstablishment", alias='@type')
    

