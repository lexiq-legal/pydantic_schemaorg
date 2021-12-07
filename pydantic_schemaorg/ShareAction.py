from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class ShareAction(CommunicateAction):
    """The act of distributing content to people for their amusement or edification.

    See https://schema.org/ShareAction.

    """
    type_: str = Field("ShareAction", const=True, alias='@type')
    

ShareAction.update_forward_refs()
