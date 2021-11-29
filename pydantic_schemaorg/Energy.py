from pydantic import Field
from pydantic_schemaorg.Quantity import Quantity


class Energy(Quantity):
    """Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit"
     "of measure&gt;'.

    See https://schema.org/Energy.

    """

    locals().update({"@type": Field("Energy", const=True)})


Energy.update_forward_refs()
