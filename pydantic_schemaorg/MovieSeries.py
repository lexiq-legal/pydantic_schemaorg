from pydantic import Field
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.VideoObject import VideoObject
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.MusicGroup import MusicGroup
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class MovieSeries(CreativeWorkSeries):
    """A series of movies. Included movies can be indicated with the hasPart property.

    See https://schema.org/MovieSeries.

    """

    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    trailer: Optional[Union[List[VideoObject], VideoObject]] = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
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
    actor: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    directors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    musicBy: Optional[Union[List[Union[Person, MusicGroup]], Union[Person, MusicGroup]]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    locals().update({"@type": Field("MovieSeries", const=True)})


MovieSeries.update_forward_refs()
