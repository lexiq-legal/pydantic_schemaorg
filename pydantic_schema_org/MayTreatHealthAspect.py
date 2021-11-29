from pydantic import Field
from pydantic_schema_org.HealthAspectEnumeration import HealthAspectEnumeration


class MayTreatHealthAspect(HealthAspectEnumeration):
    """Related topics may be treated by a Topic.

    See https://schema.org/MayTreatHealthAspect.

    """

    locals().update({"@type": Field("MayTreatHealthAspect", const=True)})


MayTreatHealthAspect.update_forward_refs()
