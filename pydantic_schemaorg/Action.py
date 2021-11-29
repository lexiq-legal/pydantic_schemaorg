from pydantic import Field
from pydantic_schemaorg.Thing import Thing
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from datetime import datetime, time


class Action(Thing):
    """An action performed by a direct agent and indirect participants upon a direct object."
     "Optionally happens at a location with the help of an inanimate instrument. The execution"
     "of the action may produce a result. Specific action sub-type documentation specifies"
     "the exact expectation of each argument/role. See also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html)"
     "and [Actions overview document](https://schema.org/docs/actions.html).

    See https://schema.org/Action.

    """

    result: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The result produced in the action. e.g. John wrote *a book*.",
    )
    object: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The object upon which the action is carried out, whose state is kept intact or changed."
     "Also known as the semantic roles patient, affected or undergoer (which change their"
     "state) or theme (which doesn't). e.g. John read *a book*.",
    )
    participant: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with"
     "*Steve*.",
    )
    error: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="For failed actions, more information on the cause of the failure.",
    )
    location: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
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
    agent: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. *John* wrote"
     "a book.",
    )
    target: Any = Field(
        None,
        description="Indicates a target EntryPoint for an Action.",
    )
    actionStatus: Any = Field(
        None,
        description="Indicates the current disposition of the Action.",
    )
    instrument: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with *a pen*.",
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
    locals().update({"@type": Field("Action", const=True)})


Action.update_forward_refs()
