from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class Country(AdministrativeArea):
    """A country.

    See https://schema.org/Country.

    """
    type_: str = Field("Country", const=True, alias='@type')
    

Country.update_forward_refs()
