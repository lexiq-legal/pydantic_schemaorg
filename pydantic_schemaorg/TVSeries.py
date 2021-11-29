from pydantic import Field, AnyUrl
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Episode import Episode
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class TVSeries(CreativeWork, CreativeWorkSeries):
    """CreativeWorkSeries dedicated to TV broadcast and associated online delivery.

    See https://schema.org/TVSeries.

    """

    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    containsSeason: Any = Field(
        None,
        description="A season that is part of the media series.",
    )
    numberOfSeasons: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of seasons in this series.",
    )
    trailer: Any = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    episodes: Optional[Union[List[Episode], Episode]] = Field(
        None,
        description="An episode of a TV/radio series or season.",
    )
    numberOfEpisodes: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of episodes in this season or series.",
    )
    countryOfOrigin: Any = Field(
        None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    director: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    productionCompany: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The production company or studio responsible for the item e.g. series, video game, episode"
     "etc.",
    )
    seasons: Any = Field(
        None,
        description="A season in a media series.",
    )
    season: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A season in a media series.",
    )
    actor: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    episode: Optional[Union[List[Episode], Episode]] = Field(
        None,
        description="An episode of a tv, radio or game media within a series or season.",
    )
    directors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    musicBy: Union[List[Union[Person, Any]], Union[Person, Any]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    locals().update({"@type": Field("TVSeries", const=True)})


TVSeries.update_forward_refs()
