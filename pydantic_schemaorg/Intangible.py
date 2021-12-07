from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Intangible(Thing):
    """A utility class that serves as the umbrella for a number of 'intangible' things such as"
     "quantities, structured values, etc.

    See https://schema.org/Intangible.

    """
    type_: str = Field("Intangible", const=True, alias='@type')
    

Intangible.update_forward_refs()
