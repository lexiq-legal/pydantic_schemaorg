from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemMetric(SizeSystemEnumeration):
    """Metric size system.

    See: https://schema.org/SizeSystemMetric
    Model depth: 5
    """
    type_: str = Field("SizeSystemMetric", alias='@type')
    

