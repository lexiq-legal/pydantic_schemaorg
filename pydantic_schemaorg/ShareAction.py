from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class ShareAction(CommunicateAction):
    """The act of distributing content to people for their amusement or edification.

    See https://schema.org/ShareAction.

    """

    locals().update({"@type": Field("ShareAction", const=True)})


ShareAction.update_forward_refs()
