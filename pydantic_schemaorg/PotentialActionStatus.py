from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class PotentialActionStatus(ActionStatusType):
    """A description of an action that is supported.

    See https://schema.org/PotentialActionStatus.

    """

    locals().update({"@type": Field("PotentialActionStatus", const=True)})


PotentialActionStatus.update_forward_refs()
