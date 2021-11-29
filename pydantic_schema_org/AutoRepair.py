from pydantic import Field
from pydantic_schema_org.AutomotiveBusiness import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """Car repair business.

    See https://schema.org/AutoRepair.

    """

    locals().update({"@type": Field("AutoRepair", const=True)})


AutoRepair.update_forward_refs()
