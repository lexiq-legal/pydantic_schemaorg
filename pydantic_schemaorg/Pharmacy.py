from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore.

    See https://schema.org/Pharmacy.

    """

    locals().update({"@type": Field("Pharmacy", const=True)})


Pharmacy.update_forward_refs()
