from pydantic import Field
from pydantic_schemaorg.Offer import Offer
from typing import List, Optional, Union
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Intangible import Intangible


class MediaSubscription(Intangible):
    """A subscription which allows a user to access media including audio, video, books, etc.

    See https://schema.org/MediaSubscription.

    """
    type_: str = Field("MediaSubscription", const=True, alias='@type')
    expectsAcceptanceOf: Optional[Union[List[Union[Offer, str]], Union[Offer, str]]] = Field(
        None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    authenticator: Optional[Union[List[Union[Organization, str]], Union[Organization, str]]] = Field(
        None,
        description="The Organization responsible for authenticating the user's subscription. For example,"
     "many media apps require a cable/satellite provider to authenticate your subscription"
     "before playing media.",
    )
    

MediaSubscription.update_forward_refs()
