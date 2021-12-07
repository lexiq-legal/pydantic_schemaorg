from pydantic import Field
from pydantic_schemaorg.LegalService import LegalService


class Attorney(LegalService):
    """Professional service: Attorney. This type is deprecated - [[LegalService]] is more"
     "inclusive and less ambiguous.

    See https://schema.org/Attorney.

    """
    type_: str = Field("Attorney", const=True, alias='@type')
    

Attorney.update_forward_refs()
