from pydantic import Field
from pydantic_schema_org.Offer import Offer
from typing import Any, Optional, Union, List
from pydantic_schema_org.Organization import Organization
from pydantic_schema_org.Intangible import Intangible


class MediaSubscription(Intangible):
    """A subscription which allows a user to access media including audio, video, books, etc.

    See https://schema.org/MediaSubscription.

    """

    expectsAcceptanceOf: Optional[Union[List[Offer], Offer]] = Field(
        None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    authenticator: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The Organization responsible for authenticating the user's subscription. For example,"
     "many media apps require a cable/satellite provider to authenticate your subscription"
     "before playing media.",
    )
    locals().update({"@type": Field("MediaSubscription", const=True)})


MediaSubscription.update_forward_refs()
