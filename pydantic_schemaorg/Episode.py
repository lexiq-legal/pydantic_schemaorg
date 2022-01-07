from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
from typing import List, Optional, Union
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.VideoObject import VideoObject
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
from pydantic_schemaorg.MusicGroup import MusicGroup
from pydantic_schemaorg.CreativeWork import CreativeWork


class Episode(CreativeWork):
    """A media episode (e.g. TV, radio, video game) which can be part of a series or season.

    See https://schema.org/Episode.

    """
    type_: str = Field("Episode", const=True, alias='@type')
    partOfSeason: Optional[Union[List[Union[CreativeWorkSeason, str]], Union[CreativeWorkSeason, str]]] = Field(
        None,
        description="The season to which this episode belongs.",
    )
    actors: Optional[Union[List[Union[Person, str]], Union[Person, str]]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    episodeNumber: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="Position of the episode within an ordered group of episodes.",
    )
    trailer: Optional[Union[List[Union[VideoObject, str]], Union[VideoObject, str]]] = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    duration: Optional[Union[List[Union[Duration, str]], Union[Duration, str]]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    director: Optional[Union[List[Union[Person, str]], Union[Person, str]]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    productionCompany: Optional[Union[List[Union[Organization, str]], Union[Organization, str]]] = Field(
        None,
        description="The production company or studio responsible for the item e.g. series, video game, episode"
     "etc.",
    )
    partOfSeries: Optional[Union[List[Union[CreativeWorkSeries, str]], Union[CreativeWorkSeries, str]]] = Field(
        None,
        description="The series to which this episode or season belongs.",
    )
    actor: Optional[Union[List[Union[Person, str]], Union[Person, str]]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    directors: Optional[Union[List[Union[Person, str]], Union[Person, str]]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    musicBy: Optional[Union[List[Union[MusicGroup, Person, str]], Union[MusicGroup, Person, str]]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    

Episode.update_forward_refs()
