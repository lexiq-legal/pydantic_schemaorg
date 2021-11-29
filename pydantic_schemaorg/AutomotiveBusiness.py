from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """Car repair, sales, or parts.

    See https://schema.org/AutomotiveBusiness.

    """

    locals().update({"@type": Field("AutomotiveBusiness", const=True)})


AutomotiveBusiness.update_forward_refs()
