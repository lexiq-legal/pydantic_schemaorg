from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """A courthouse.

    See: https://schema.org/Courthouse
    Model depth: 5
    """
    type_: str = Field("Courthouse", alias='@type')
    

