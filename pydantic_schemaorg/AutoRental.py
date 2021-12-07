from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """A car rental business.

    See https://schema.org/AutoRental.

    """
    type_: str = Field("AutoRental", const=True, alias='@type')
    

AutoRental.update_forward_refs()
