from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class PET(MedicalImagingTechnique):
    """Positron emission tomography imaging.

    See https://schema.org/PET.

    """

    locals().update({"@type": Field("PET", const=True)})


PET.update_forward_refs()
