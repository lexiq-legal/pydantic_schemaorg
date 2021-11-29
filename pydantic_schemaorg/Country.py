from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class Country(AdministrativeArea):
    """A country.

    See https://schema.org/Country.

    """

    locals().update({"@type": Field("Country", const=True)})


Country.update_forward_refs()
