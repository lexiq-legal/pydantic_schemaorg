from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """An employment agency.

    See https://schema.org/EmploymentAgency.

    """
    type_: str = Field("EmploymentAgency", const=True, alias='@type')
    

EmploymentAgency.update_forward_refs()
