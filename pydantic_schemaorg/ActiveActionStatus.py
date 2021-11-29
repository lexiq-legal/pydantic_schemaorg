from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class ActiveActionStatus(ActionStatusType):
    """An in-progress action (e.g, while watching the movie, or driving to a location).

    See https://schema.org/ActiveActionStatus.

    """

    locals().update({"@type": Field("ActiveActionStatus", const=True)})


ActiveActionStatus.update_forward_refs()
