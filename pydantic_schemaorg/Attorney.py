from pydantic import Field
from pydantic_schemaorg.LegalService import LegalService


class Attorney(LegalService):
    """Professional service: Attorney. This type is deprecated - [[LegalService]] is more"
     "inclusive and less ambiguous.

    See https://schema.org/Attorney.

    """

    locals().update({"@type": Field("Attorney", const=True)})


Attorney.update_forward_refs()
