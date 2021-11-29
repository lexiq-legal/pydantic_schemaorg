from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalOrganization import MedicalOrganization


class Dentist(LocalBusiness, MedicalBusiness, MedicalOrganization):
    """A dentist.

    See https://schema.org/Dentist.

    """

    locals().update({"@type": Field("Dentist", const=True)})


Dentist.update_forward_refs()
