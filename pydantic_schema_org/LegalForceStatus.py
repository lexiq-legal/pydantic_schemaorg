from pydantic import Field
from pydantic_schema_org.StatusEnumeration import StatusEnumeration


class LegalForceStatus(StatusEnumeration):
    """A list of possible statuses for the legal force of a legislation.

    See https://schema.org/LegalForceStatus.

    """

    locals().update({"@type": Field("LegalForceStatus", const=True)})


LegalForceStatus.update_forward_refs()
