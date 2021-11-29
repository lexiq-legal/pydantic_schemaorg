from pydantic import Field
from pydantic_schema_org.HealthAspectEnumeration import HealthAspectEnumeration


class ContagiousnessHealthAspect(HealthAspectEnumeration):
    """Content about contagion mechanisms and contagiousness information over the topic.

    See https://schema.org/ContagiousnessHealthAspect.

    """

    locals().update({"@type": Field("ContagiousnessHealthAspect", const=True)})


ContagiousnessHealthAspect.update_forward_refs()
