from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class GettingAccessHealthAspect(HealthAspectEnumeration):
    """Content that discusses practical and policy aspects for getting access to specific"
     "kinds of healthcare (e.g. distribution mechanisms for vaccines).

    See https://schema.org/GettingAccessHealthAspect.

    """

    locals().update({"@type": Field("GettingAccessHealthAspect", const=True)})


GettingAccessHealthAspect.update_forward_refs()
