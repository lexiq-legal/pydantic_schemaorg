from pydantic import Field, AnyUrl
from pydantic_schemaorg.Language import Language
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Country import Country
from pydantic_schemaorg.TVSeries import TVSeries
from pydantic_schemaorg.Episode import Episode


class TVEpisode(Episode):
    """A TV episode which can be part of a series or season.

    See https://schema.org/TVEpisode.

    """

    subtitleLanguage: Optional[Union[List[Union[str, Language]], Union[str, Language]]] = Field(
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
    partOfTVSeries: Optional[Union[List[TVSeries], TVSeries]] = Field(
        None,
        description="The TV series to which this episode or season belongs.",
    )
    locals().update({"@type": Field("TVEpisode", const=True)})


TVEpisode.update_forward_refs()
