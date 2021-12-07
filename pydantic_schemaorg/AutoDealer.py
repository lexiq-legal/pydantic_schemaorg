from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """An car dealership.

    See https://schema.org/AutoDealer.

    """
    type_: str = Field("AutoDealer", const=True, alias='@type')
    

AutoDealer.update_forward_refs()
