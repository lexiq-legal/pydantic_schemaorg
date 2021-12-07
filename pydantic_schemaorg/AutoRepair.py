from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """Car repair business.

    See https://schema.org/AutoRepair.

    """
    type_: str = Field("AutoRepair", const=True, alias='@type')
    

AutoRepair.update_forward_refs()
