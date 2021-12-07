from pydantic import Field
from pydantic_schemaorg.Quantity import Quantity


class Energy(Quantity):
    """Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit"
     "of measure&gt;'.

    See https://schema.org/Energy.

    """
    type_: str = Field("Energy", const=True, alias='@type')
    

Energy.update_forward_refs()
