from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class GovernmentOffice(LocalBusiness):
    """A government office&#x2014;for example, an IRS or DMV office.

    See https://schema.org/GovernmentOffice.

    """
    type_: str = Field("GovernmentOffice", const=True, alias='@type')
    

GovernmentOffice.update_forward_refs()
