from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
from pydantic_schemaorg.CreativeWork import CreativeWork


class TVSeason(CreativeWorkSeason, CreativeWork):
    """Season dedicated to TV broadcast and associated online delivery.

    See: https://schema.org/TVSeason
    Model depth: 3
    """
    type_: str = Field("TVSeason", alias='@type')
    countryOfOrigin: Optional[Union[List[Union['Country', str]], 'Country', str]] = Field(
        None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    partOfTVSeries: Optional[Union[List[Union['TVSeries', str]], 'TVSeries', str]] = Field(
        None,
        description="The TV series to which this episode or season belongs.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.TVSeries import TVSeries
