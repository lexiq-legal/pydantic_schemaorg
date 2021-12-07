from pydantic import Field
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod


class OnSitePickup(DeliveryMethod):
    """A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.

    See https://schema.org/OnSitePickup.

    """
    type_: str = Field("OnSitePickup", const=True, alias='@type')
    

OnSitePickup.update_forward_refs()
