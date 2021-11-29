from pydantic import Field
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalOrganization import MedicalOrganization


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore.

    See https://schema.org/Pharmacy.

    """

    locals().update({"@type": Field("Pharmacy", const=True)})


Pharmacy.update_forward_refs()
