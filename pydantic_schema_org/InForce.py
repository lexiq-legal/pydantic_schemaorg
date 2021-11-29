from pydantic import Field
from pydantic_schema_org.LegalForceStatus import LegalForceStatus


class InForce(LegalForceStatus):
    """Indicates that a legislation is in force.

    See https://schema.org/InForce.

    """

    locals().update({"@type": Field("InForce", const=True)})


InForce.update_forward_refs()
