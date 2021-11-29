from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Demand import Demand
from datetime import date, datetime, time
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.EventStatusType import EventStatusType
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Review import Review


class Event(Thing):
    """An event happening at a certain time and location, such as a concert, lecture, or festival."
     "Ticketing information may be added via the [[offers]] property. Repeated events may"
     "be structured as separate Event objects.

    See https://schema.org/Event.

    """

    subEvent: Any = Field(
        None,
        description="An Event that is part of this event. For example, a conference event includes many presentations,"
     "each of which is a subEvent of the conference.",
    )
    about: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The subject matter of the content.",
    )
    offers: Union[List[Union[Demand, Any]], Union[Demand, Any]] = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    doorTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The time admission will commence.",
    )
    typicalAgeRange: Optional[Union[List[str], str]] = Field(
        None,
        description="The typical expected age range, e.g. '7-9', '11-'.",
    )
    funder: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    maximumAttendeeCapacity: Optional[Union[List[int], int]] = Field(
        None,
        description="The total number of individuals that may attend an event or venue.",
    )
    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    attendees: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A person attending the event.",
    )
    composer: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed"
     "at some event.",
    )
    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    translator: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="Organization or person who adapts a creative work to different languages, regional"
     "differences and technical requirements of a target market, or that translates during"
     "some event.",
    )
    previousStartDate: Optional[Union[List[date], date]] = Field(
        None,
        description="Used in conjunction with eventStatus for rescheduled or cancelled events. This property"
     "contains the previously scheduled start date. For rescheduled events, the startDate"
     "property should be used for the newly scheduled start date. In the (rare) case of an event"
     "that has been postponed and rescheduled multiple times, this field may be repeated.",
    )
    director: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    location: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    eventStatus: Optional[Union[List[EventStatusType], EventStatusType]] = Field(
        None,
        description="An eventStatus of an event represents its status; particularly useful when an event"
     "is cancelled or rescheduled.",
    )
    maximumPhysicalAttendeeCapacity: Optional[Union[List[int], int]] = Field(
        None,
        description="The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]]"
     "is [[OfflineEventAttendanceMode]] (or the offline aspects, in the case of a [[MixedEventAttendanceMode]]).",
    )
    remainingAttendeeCapacity: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of attendee places for an event that remain unallocated.",
    )
    attendee: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A person or organization attending the event.",
    )
    endDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    audience: Optional[Union[List[Audience], Audience]] = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    sponsor: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    organizer: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="An organizer of an Event.",
    )
    actor: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    workFeatured: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="A work featured in some event, e.g. exhibited in an ExhibitionEvent. Specific subproperties"
     "are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).",
    )
    eventAttendanceMode: Any = Field(
        None,
        description="The eventAttendanceMode of an event indicates whether it occurs online, offline, or"
     "a mix.",
    )
    superEvent: Any = Field(
        None,
        description="An event that this event is a part of. For example, a collection of individual music performances"
     "might each have a music festival as their superEvent.",
    )
    workPerformed: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="A work performed in some event, for example a play performed in a TheaterEvent.",
    )
    recordedIn: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="The CreativeWork that captured all or part of this Event.",
    )
    performers: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The main performer or performers of the event&#x2014;for example, a presenter, musician,"
     "or actor.",
    )
    maximumVirtualAttendeeCapacity: Optional[Union[List[int], int]] = Field(
        None,
        description="The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]]"
     "is [[OnlineEventAttendanceMode]] (or the online aspects, in the case of a [[MixedEventAttendanceMode]]).",
    )
    startDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    inLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    performer: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A performer at the event&#x2014;for example, a presenter, musician, musical group"
     "or actor.",
    )
    review: Optional[Union[List[Review], Review]] = Field(
        None,
        description="A review of the item.",
    )
    subEvents: Any = Field(
        None,
        description="Events that are a part of this event. For example, a conference event includes many presentations,"
     "each subEvents of the conference.",
    )
    eventSchedule: Any = Field(
        None,
        description="Associates an [[Event]] with a [[Schedule]]. There are circumstances where it is preferable"
     "to share a schedule for a series of repeating events rather than data on the individual"
     "events themselves. For example, a website or application might prefer to publish a schedule"
     "for a weekly gym class rather than provide data on every event. A schedule could be processed"
     "by applications to add forthcoming events to a calendar. An [[Event]] that is associated"
     "with a [[Schedule]] using this property should not have [[startDate]] or [[endDate]]"
     "properties. These are instead defined within the associated [[Schedule]], this avoids"
     "any ambiguity for clients using the data. The property might have repeated values to"
     "specify different schedules, e.g. for different months or seasons.",
    )
    contributor: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A secondary contributor to the CreativeWork or Event.",
    )
    isAccessibleForFree: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    locals().update({"@type": Field("Event", const=True)})


Event.update_forward_refs()
