from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class CompletedActionStatus(ActionStatusType):
    """An action that has already taken place.

    See https://schema.org/CompletedActionStatus.

    """

    locals().update({"@type": Field("CompletedActionStatus", const=True)})


CompletedActionStatus.update_forward_refs()
