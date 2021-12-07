from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RealEstateAgent(LocalBusiness):
    """A real-estate agent.

    See https://schema.org/RealEstateAgent.

    """
    type_: str = Field("RealEstateAgent", const=True, alias='@type')
    

RealEstateAgent.update_forward_refs()
