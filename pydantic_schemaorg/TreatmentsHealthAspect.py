from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class TreatmentsHealthAspect(HealthAspectEnumeration):
    """Treatments or related therapies for a Topic.

    See https://schema.org/TreatmentsHealthAspect.

    """
    type_: str = Field("TreatmentsHealthAspect", const=True, alias='@type')
    

TreatmentsHealthAspect.update_forward_refs()
