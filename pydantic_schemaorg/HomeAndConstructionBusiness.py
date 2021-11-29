from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class HomeAndConstructionBusiness(LocalBusiness):
    """A construction business. A HomeAndConstructionBusiness is a [[LocalBusiness]] that"
     "provides services around homes and buildings. As a [[LocalBusiness]] it can be described"
     "as a [[provider]] of one or more [[Service]]\(s).

    See https://schema.org/HomeAndConstructionBusiness.

    """

    locals().update({"@type": Field("HomeAndConstructionBusiness", const=True)})


HomeAndConstructionBusiness.update_forward_refs()
