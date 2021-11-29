from pydantic import Field
from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemMetric(SizeSystemEnumeration):
    """Metric size system.

    See https://schema.org/SizeSystemMetric.

    """

    locals().update({"@type": Field("SizeSystemMetric", const=True)})


SizeSystemMetric.update_forward_refs()
