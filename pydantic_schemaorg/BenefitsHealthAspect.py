from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class BenefitsHealthAspect(HealthAspectEnumeration):
    """Content about the benefits and advantages of usage or utilization of topic.

    See https://schema.org/BenefitsHealthAspect.

    """

    locals().update({"@type": Field("BenefitsHealthAspect", const=True)})


BenefitsHealthAspect.update_forward_refs()
