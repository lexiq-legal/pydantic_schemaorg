from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class OverviewHealthAspect(HealthAspectEnumeration):
    """Overview of the content. Contains a summarized view of the topic with the most relevant"
     "information for an introduction.

    See https://schema.org/OverviewHealthAspect.

    """

    locals().update({"@type": Field("OverviewHealthAspect", const=True)})


OverviewHealthAspect.update_forward_refs()
