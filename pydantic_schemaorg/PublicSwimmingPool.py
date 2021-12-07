from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """A public swimming pool.

    See https://schema.org/PublicSwimmingPool.

    """
    type_: str = Field("PublicSwimmingPool", const=True, alias='@type')
    

PublicSwimmingPool.update_forward_refs()
