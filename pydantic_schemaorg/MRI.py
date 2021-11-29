from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class MRI(MedicalImagingTechnique):
    """Magnetic resonance imaging.

    See https://schema.org/MRI.

    """

    locals().update({"@type": Field("MRI", const=True)})


MRI.update_forward_refs()
