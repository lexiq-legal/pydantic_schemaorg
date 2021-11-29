from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class PharmacySpecialty(MedicalSpecialty):
    """The practice or art and science of preparing and dispensing drugs and medicines.

    See https://schema.org/PharmacySpecialty.

    """

    locals().update({"@type": Field("PharmacySpecialty", const=True)})


PharmacySpecialty.update_forward_refs()
