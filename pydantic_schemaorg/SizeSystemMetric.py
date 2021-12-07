from pydantic import Field
from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemMetric(SizeSystemEnumeration):
    """Metric size system.

    See https://schema.org/SizeSystemMetric.

    """
    type_: str = Field("SizeSystemMetric", const=True, alias='@type')
    

SizeSystemMetric.update_forward_refs()
