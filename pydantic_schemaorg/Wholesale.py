from pydantic import Field
from pydantic_schemaorg.DrugCostCategory import DrugCostCategory


class Wholesale(DrugCostCategory):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    See https://schema.org/Wholesale.

    """

    locals().update({"@type": Field("Wholesale", const=True)})


Wholesale.update_forward_refs()
