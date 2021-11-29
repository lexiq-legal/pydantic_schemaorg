from pydantic import Field
from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class NotInForce(LegalForceStatus):
    """Indicates that a legislation is currently not in force.

    See https://schema.org/NotInForce.

    """

    locals().update({"@type": Field("NotInForce", const=True)})


NotInForce.update_forward_refs()
