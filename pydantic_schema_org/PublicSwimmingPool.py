from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """A public swimming pool.

    See https://schema.org/PublicSwimmingPool.

    """

    locals().update({"@type": Field("PublicSwimmingPool", const=True)})


PublicSwimmingPool.update_forward_refs()
