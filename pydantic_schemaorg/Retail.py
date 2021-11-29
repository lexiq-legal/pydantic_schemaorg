from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory


class Retail(DrugCostCategory):
    """The drug's cost represents the retail cost of the drug.

    See https://schema.org/Retail.

    """

    locals().update({"@type": Field("Retail", const=True)})


Retail.update_forward_refs()
