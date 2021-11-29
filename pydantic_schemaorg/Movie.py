from pydantic import Field, AnyUrl
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.Country import Country
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.CreativeWork import CreativeWork


class Movie(CreativeWork):
    """A movie.

    See https://schema.org/Movie.

    """

    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    trailer: Any = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    duration: Optional[Union[List[Duration], Duration]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    subtitleLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )
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
    titleEIDR: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]]"
     "representing at the most general/abstract level, a work of film or television. For example,"
     "the motion picture known as \"Ghostbusters\" has a titleEIDR of \"10.5240/7EC7-228A-510A-053E-CBB8-J\"."
     "This title (or work) may have several variants, which EIDR calls \"edits\". See [[editEIDR]]."
     "Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and"
     "their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general"
     "description), or alongside [[editEIDR]] for a more edit-specific description.",
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
    locals().update({"@type": Field("Movie", const=True)})


Movie.update_forward_refs()
