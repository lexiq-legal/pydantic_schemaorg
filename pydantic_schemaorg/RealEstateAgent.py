from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RealEstateAgent(LocalBusiness):
    """A real-estate agent.

    See https://schema.org/RealEstateAgent.

    """

    locals().update({"@type": Field("RealEstateAgent", const=True)})


RealEstateAgent.update_forward_refs()
