from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ChildCare(LocalBusiness):
    """A Childcare center.

    See https://schema.org/ChildCare.

    """

    locals().update({"@type": Field("ChildCare", const=True)})


ChildCare.update_forward_refs()
