from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PhysicalActivityCategory(Enumeration):
    """Categories of physical activity, organized by physiologic classification.

    See: https://schema.org/PhysicalActivityCategory
    Model depth: 4
    """
    type_: str = Field("PhysicalActivityCategory", alias='@type')
    

