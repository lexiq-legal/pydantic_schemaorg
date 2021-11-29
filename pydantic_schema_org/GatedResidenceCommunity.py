from pydantic import Field
from pydantic_schema_org.Residence import Residence


class GatedResidenceCommunity(Residence):
    """Residence type: Gated community.

    See https://schema.org/GatedResidenceCommunity.

    """

    locals().update({"@type": Field("GatedResidenceCommunity", const=True)})


GatedResidenceCommunity.update_forward_refs()
