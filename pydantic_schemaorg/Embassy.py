from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """An embassy.

    See https://schema.org/Embassy.

    """
    type_: str = Field("Embassy", const=True, alias='@type')
    

Embassy.update_forward_refs()
