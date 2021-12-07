from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class TaxiStand(CivicStructure):
    """A taxi stand.

    See https://schema.org/TaxiStand.

    """
    type_: str = Field("TaxiStand", const=True, alias='@type')
    

TaxiStand.update_forward_refs()
