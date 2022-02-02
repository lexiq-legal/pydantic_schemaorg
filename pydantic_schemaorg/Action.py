from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from datetime import time


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Action(Thing):
    """An action performed by a direct agent and indirect participants upon a direct object."
     "Optionally happens at a location with the help of an inanimate instrument. The execution"
     "of the action may produce a result. Specific action sub-type documentation specifies"
     "the exact expectation of each argument/role. See also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html)"
     "and [Actions overview document](https://schema.org/docs/actions.html).

    See: https://schema.org/Action
    Model depth: 2
    """
    type_: str = Field("Action", alias='@type')
    result: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="The result produced in the action. e.g. John wrote *a book*.",
    )
    object: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="The object upon which the action is carried out, whose state is kept intact or changed."
     "Also known as the semantic roles patient, affected or undergoer (which change their"
     "state) or theme (which doesn't). e.g. John read *a book*.",
    )
    participant: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with"
     "*Steve*.",
    )
    error: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="For failed actions, more information on the cause of the failure.",
    )
    location: Optional[Union[List[Union[str, 'Text', 'PostalAddress', 'Place', 'VirtualLocation']], str, 'Text', 'PostalAddress', 'Place', 'VirtualLocation']] = Field(
        None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    endTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    agent: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. *John* wrote"
     "a book.",
    )
    target: Optional[Union[List[Union['EntryPoint', str]], 'EntryPoint', str]] = Field(
        None,
        description="Indicates a target EntryPoint for an Action.",
    )
    actionStatus: Optional[Union[List[Union['ActionStatusType', str]], 'ActionStatusType', str]] = Field(
        None,
        description="Indicates the current disposition of the Action.",
    )
    instrument: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with *a pen*.",
    )
    startTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.EntryPoint import EntryPoint
    from pydantic_schemaorg.ActionStatusType import ActionStatusType
