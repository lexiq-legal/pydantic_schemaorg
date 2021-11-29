from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """A recycling center.

    See https://schema.org/RecyclingCenter.

    """

    locals().update({"@type": Field("RecyclingCenter", const=True)})


RecyclingCenter.update_forward_refs()
