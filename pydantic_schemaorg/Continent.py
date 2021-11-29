from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Continent(Landform):
    """One of the continents (for example, Europe or Africa).

    See https://schema.org/Continent.

    """

    locals().update({"@type": Field("Continent", const=True)})


Continent.update_forward_refs()
