from pydantic import Field
from pydantic_schemaorg.Permit import Permit


class GovernmentPermit(Permit):
    """A permit issued by a government agency.

    See https://schema.org/GovernmentPermit.

    """
    type_: str = Field("GovernmentPermit", const=True, alias='@type')
    

GovernmentPermit.update_forward_refs()
