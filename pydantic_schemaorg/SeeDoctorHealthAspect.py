from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SeeDoctorHealthAspect(HealthAspectEnumeration):
    """Information about questions that may be asked, when to see a professional, measures"
     "before seeing a doctor or content about the first consultation.

    See https://schema.org/SeeDoctorHealthAspect.

    """
    type_: str = Field("SeeDoctorHealthAspect", const=True, alias='@type')
    

SeeDoctorHealthAspect.update_forward_refs()
