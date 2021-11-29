from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """A car wash business.

    See https://schema.org/AutoWash.

    """

    locals().update({"@type": Field("AutoWash", const=True)})


AutoWash.update_forward_refs()
