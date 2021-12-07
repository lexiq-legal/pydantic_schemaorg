from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """A courthouse.

    See https://schema.org/Courthouse.

    """
    type_: str = Field("Courthouse", const=True, alias='@type')
    

Courthouse.update_forward_refs()
