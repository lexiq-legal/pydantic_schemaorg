from pydantic import Field
from pydantic_schema_org.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemMetric(SizeSystemEnumeration):
    """Metric size system.

    See https://schema.org/SizeSystemMetric.

    """

    locals().update({"@type": Field("SizeSystemMetric", const=True)})


SizeSystemMetric.update_forward_refs()
