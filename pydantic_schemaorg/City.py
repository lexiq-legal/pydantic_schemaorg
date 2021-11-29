from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class City(AdministrativeArea):
    """A city or town.

    See https://schema.org/City.

    """

    locals().update({"@type": Field("City", const=True)})


City.update_forward_refs()
