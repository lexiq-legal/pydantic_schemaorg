from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """An employment agency.

    See https://schema.org/EmploymentAgency.

    """

    locals().update({"@type": Field("EmploymentAgency", const=True)})


EmploymentAgency.update_forward_refs()
