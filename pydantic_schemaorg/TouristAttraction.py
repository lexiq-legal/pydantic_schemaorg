from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Place import Place


class TouristAttraction(Place):
    """A tourist attraction. In principle any Thing can be a [[TouristAttraction]], from a"
     "[[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]]. This"
     "Type can be used on its own to describe a general [[TouristAttraction]], or be used as"
     "an [[additionalType]] to add tourist attraction properties to any other type. (See"
     "examples below)

    See https://schema.org/TouristAttraction.

    """

    availableLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]]",
    )
    touristType: Optional[Union[List[Union[str, Audience]], Union[str, Audience]]] = Field(
        None,
        description="Attraction suitable for type(s) of tourist. eg. Children, visitors from a particular"
     "country, etc.",
    )
    locals().update({"@type": Field("TouristAttraction", const=True)})


TouristAttraction.update_forward_refs()
