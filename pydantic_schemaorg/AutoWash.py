from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """A car wash business.

    See https://schema.org/AutoWash.

    """
    type_: str = Field("AutoWash", const=True, alias='@type')
    

AutoWash.update_forward_refs()
