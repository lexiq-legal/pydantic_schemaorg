from pydantic import Field
from pydantic_schema_org.AutomotiveBusiness import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """A car wash business.

    See https://schema.org/AutoWash.

    """

    locals().update({"@type": Field("AutoWash", const=True)})


AutoWash.update_forward_refs()
