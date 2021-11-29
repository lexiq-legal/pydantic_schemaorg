from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
from pydantic_schemaorg.CreativeWork import CreativeWork


class Episode(CreativeWork):
    """A media episode (e.g. TV, radio, video game) which can be part of a series or season.

    See https://schema.org/Episode.

    """

    partOfSeason: Any = Field(
        None,
        description="The season to which this episode belongs.",
    )
    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    episodeNumber: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="Position of the episode within an ordered group of episodes.",
    )
    trailer: Any = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
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
    partOfSeries: Optional[Union[List[CreativeWorkSeries], CreativeWorkSeries]] = Field(
        None,
        description="The series to which this episode or season belongs.",
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
    musicBy: Union[List[Union[Person, Any]], Union[Person, Any]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    locals().update({"@type": Field("Episode", const=True)})


Episode.update_forward_refs()
