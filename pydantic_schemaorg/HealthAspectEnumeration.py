from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class HealthAspectEnumeration(Enumeration):
    """HealthAspectEnumeration enumerates several aspects of health content online, each"
     "of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

    See https://schema.org/HealthAspectEnumeration.

    """

    locals().update({"@type": Field("HealthAspectEnumeration", const=True)})


HealthAspectEnumeration.update_forward_refs()
