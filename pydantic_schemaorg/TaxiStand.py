from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class TaxiStand(CivicStructure):
    """A taxi stand.

    See https://schema.org/TaxiStand.

    """

    locals().update({"@type": Field("TaxiStand", const=True)})


TaxiStand.update_forward_refs()
