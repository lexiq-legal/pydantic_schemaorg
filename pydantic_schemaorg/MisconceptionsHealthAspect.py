from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class MisconceptionsHealthAspect(HealthAspectEnumeration):
    """Content about common misconceptions and myths that are related to a topic.

    See https://schema.org/MisconceptionsHealthAspect.

    """

    locals().update({"@type": Field("MisconceptionsHealthAspect", const=True)})


MisconceptionsHealthAspect.update_forward_refs()
