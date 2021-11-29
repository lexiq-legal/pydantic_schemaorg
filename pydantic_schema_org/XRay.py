from pydantic import Field
from pydantic_schema_org.MedicalImagingTechnique import MedicalImagingTechnique


class XRay(MedicalImagingTechnique):
    """X-ray imaging.

    See https://schema.org/XRay.

    """

    locals().update({"@type": Field("XRay", const=True)})


XRay.update_forward_refs()
