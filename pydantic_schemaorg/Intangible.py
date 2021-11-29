from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Intangible(Thing):
    """A utility class that serves as the umbrella for a number of 'intangible' things such as"
     "quantities, structured values, etc.

    See https://schema.org/Intangible.

    """

    locals().update({"@type": Field("Intangible", const=True)})


Intangible.update_forward_refs()
