from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Registry(MedicalObservationalStudyDesign):
    """A registry-based study design.

    See https://schema.org/Registry.

    """
    type_: str = Field("Registry", const=True, alias='@type')
    

Registry.update_forward_refs()
