from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class City(AdministrativeArea):
    """A city or town.

    See https://schema.org/City.

    """
    type_: str = Field("City", const=True, alias='@type')
    

City.update_forward_refs()
