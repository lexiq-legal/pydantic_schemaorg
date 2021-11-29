from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PhysicalActivityCategory(Enumeration):
    """Categories of physical activity, organized by physiologic classification.

    See https://schema.org/PhysicalActivityCategory.

    """

    locals().update({"@type": Field("PhysicalActivityCategory", const=True)})


PhysicalActivityCategory.update_forward_refs()
