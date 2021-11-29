from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class HowOrWhereHealthAspect(HealthAspectEnumeration):
    """Information about how or where to find a topic. Also may contain location data that can"
     "be used for where to look for help if the topic is observed.

    See https://schema.org/HowOrWhereHealthAspect.

    """

    locals().update({"@type": Field("HowOrWhereHealthAspect", const=True)})


HowOrWhereHealthAspect.update_forward_refs()
