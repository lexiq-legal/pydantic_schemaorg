from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class StructuredValue(Intangible):
    """Structured values are used when the value of a property has a more complex structure than"
     "simply being a textual value or a reference to another thing.

    See https://schema.org/StructuredValue.

    """

    locals().update({"@type": Field("StructuredValue", const=True)})


StructuredValue.update_forward_refs()
