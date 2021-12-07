from pydantic import Field
from pydantic_schemaorg.Audience import Audience


class Researcher(Audience):
    """Researchers.

    See https://schema.org/Researcher.

    """
    type_: str = Field("Researcher", const=True, alias='@type')
    

Researcher.update_forward_refs()
