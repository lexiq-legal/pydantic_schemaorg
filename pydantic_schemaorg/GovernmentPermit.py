from pydantic import Field
from pydantic_schemaorg.Permit import Permit


class GovernmentPermit(Permit):
    """A permit issued by a government agency.

    See https://schema.org/GovernmentPermit.

    """

    locals().update({"@type": Field("GovernmentPermit", const=True)})


GovernmentPermit.update_forward_refs()
