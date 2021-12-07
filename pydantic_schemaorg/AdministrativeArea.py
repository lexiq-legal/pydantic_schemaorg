from pydantic import Field
from pydantic_schemaorg.Place import Place


class AdministrativeArea(Place):
    """A geographical region, typically under the jurisdiction of a particular government.

    See https://schema.org/AdministrativeArea.

    """
    type_: str = Field("AdministrativeArea", const=True, alias='@type')
    

AdministrativeArea.update_forward_refs()
