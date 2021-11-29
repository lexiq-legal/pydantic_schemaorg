from pydantic import Field, AnyUrl, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Place import Place
from datetime import date, datetime, time
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.NewsArticle import NewsArticle


class MediaObject(CreativeWork):
    """A media object, such as an image, video, or audio object embedded in a web page or a downloadable"
     "dataset i.e. DataDownload. Note that a creative work may have many media objects associated"
     "with it on the same web page. For example, a page about a single song (MusicRecording)"
     "may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).

    See https://schema.org/MediaObject.

    """

    bitrate: Optional[Union[List[str], str]] = Field(
        None,
        description="The bitrate of the media object.",
    )
    contentUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="Actual bytes of the media object, for example the image file or video file.",
    )
    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    productionCompany: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The production company or studio responsible for the item e.g. series, video game, episode"
     "etc.",
    )
    regionsAllowed: Optional[Union[List[Place], Place]] = Field(
        None,
        description="The regions where the media is allowed. If not specified, then it's assumed to be allowed"
     "everywhere. Specify the countries in [ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166).",
    )
    requiresSubscription: Union[List[Union[StrictBool, Any]], Union[StrictBool, Any]] = Field(
        None,
        description="Indicates if use of the media require a subscription (either paid or free). Allowed values"
     "are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').",
    )
    uploadDate: Optional[Union[List[date], date]] = Field(
        None,
        description="Date when this media object was uploaded to this site.",
    )
    height: Any = Field(
        None,
        description="The height of the item.",
    )
    endTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    sha256: Optional[Union[List[str], str]] = Field(
        None,
        description="The [SHA-2](https://en.wikipedia.org/wiki/SHA-2) SHA256 hash of the content of"
     "the item. For example, a zero-length input has value 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'",
    )
    encodesCreativeWork: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="The CreativeWork encoded by this media object.",
    )
    associatedArticle: Optional[Union[List[NewsArticle], NewsArticle]] = Field(
        None,
        description="A NewsArticle associated with the Media Object.",
    )
    width: Any = Field(
        None,
        description="The width of the item.",
    )
    embedUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A URL pointing to a player for a specific video. In general, this is the information in"
     "the ```src``` element of an ```embed``` tag and should not be the same as the content of"
     "the ```loc``` tag.",
    )
    encodingFormat: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)"
     "and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types))"
     "e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.)."
     "In cases where a [[CreativeWork]] has several media type representations, [[encoding]]"
     "can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]]"
     "information. Unregistered or niche encoding and file formats can be indicated instead"
     "via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.",
    )
    interpretedAsClaim: Any = Field(
        None,
        description="Used to indicate a specific claim contained, implied, translated or refined from the"
     "content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can"
     "be indicated using [[claimInterpreter]].",
    )
    startTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    contentSize: Optional[Union[List[str], str]] = Field(
        None,
        description="File size in (mega/kilo) bytes.",
    )
    playerType: Optional[Union[List[str], str]] = Field(
        None,
        description="Player type required&#x2014;for example, Flash or Silverlight.",
    )
    ineligibleRegion: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    locals().update({"@type": Field("MediaObject", const=True)})


MediaObject.update_forward_refs()
