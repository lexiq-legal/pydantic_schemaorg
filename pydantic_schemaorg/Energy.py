from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Quantity import Quantity


class Energy(Quantity):
    """Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit"
     "of measure&gt;'.

    See: https://schema.org/Energy
    Model depth: 4
    """
    type_: str = Field("Energy", alias='@type')
    

