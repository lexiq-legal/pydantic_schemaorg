from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class CT(MedicalImagingTechnique):
    """X-ray computed tomography imaging.

    See https://schema.org/CT.

    """

    locals().update({"@type": Field("CT", const=True)})


CT.update_forward_refs()
