from pydantic import Field
from pydantic_schemaorg.Quantity import Quantity


class Mass(Quantity):
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of"
     "measure&gt;'. E.g., '7 kg'.

    See https://schema.org/Mass.

    """
    type_: str = Field("Mass", const=True, alias='@type')
    

Mass.update_forward_refs()
