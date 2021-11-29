from pydantic import Field
from pydantic_schemaorg.Country import Country
from typing import Any, Union, List, Optional
from pydantic_schemaorg.TVSeries import TVSeries
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason


class TVSeason(CreativeWork, CreativeWorkSeason):
    """Season dedicated to TV broadcast and associated online delivery.

    See https://schema.org/TVSeason.

    """

    countryOfOrigin: Optional[Union[List[Country], Country]] = Field(
        None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    partOfTVSeries: Optional[Union[List[TVSeries], TVSeries]] = Field(
        None,
        description="The TV series to which this episode or season belongs.",
    )
    locals().update({"@type": Field("TVSeason", const=True)})


TVSeason.update_forward_refs()
