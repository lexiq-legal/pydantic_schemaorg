from pydantic import Field
from pydantic_schemaorg.Residence import Residence


class GatedResidenceCommunity(Residence):
    """Residence type: Gated community.

    See https://schema.org/GatedResidenceCommunity.

    """
    type_: str = Field("GatedResidenceCommunity", const=True, alias='@type')
    

GatedResidenceCommunity.update_forward_refs()
