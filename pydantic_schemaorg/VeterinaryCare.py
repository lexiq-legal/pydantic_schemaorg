from pydantic import Field
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """A vet's office.

    See https://schema.org/VeterinaryCare.

    """

    locals().update({"@type": Field("VeterinaryCare", const=True)})


VeterinaryCare.update_forward_refs()
