from pydantic import Field
from pydantic_schemaorg.Place import Place


class AdministrativeArea(Place):
    """A geographical region, typically under the jurisdiction of a particular government.

    See https://schema.org/AdministrativeArea.

    """

    locals().update({"@type": Field("AdministrativeArea", const=True)})


AdministrativeArea.update_forward_refs()
