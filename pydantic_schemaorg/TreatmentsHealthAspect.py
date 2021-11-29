from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class TreatmentsHealthAspect(HealthAspectEnumeration):
    """Treatments or related therapies for a Topic.

    See https://schema.org/TreatmentsHealthAspect.

    """

    locals().update({"@type": Field("TreatmentsHealthAspect", const=True)})


TreatmentsHealthAspect.update_forward_refs()
