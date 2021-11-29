from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Optician(MedicalBusiness):
    """A store that sells reading glasses and similar devices for improving vision.

    See https://schema.org/Optician.

    """

    locals().update({"@type": Field("Optician", const=True)})


Optician.update_forward_refs()
