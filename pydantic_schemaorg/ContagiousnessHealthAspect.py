from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ContagiousnessHealthAspect(HealthAspectEnumeration):
    """Content about contagion mechanisms and contagiousness information over the topic.

    See https://schema.org/ContagiousnessHealthAspect.

    """

    locals().update({"@type": Field("ContagiousnessHealthAspect", const=True)})


ContagiousnessHealthAspect.update_forward_refs()
