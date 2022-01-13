from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DayOfWeek import DayOfWeek


class PublicHolidays(DayOfWeek):
    """This stands for any day that is a public holiday; it is a placeholder for all official public"
     "holidays in some particular location. While not technically a \"day of the week\", it"
     "can be used with [[OpeningHoursSpecification]]. In the context of an opening hours"
     "specification it can be used to indicate opening hours on public holidays, overriding"
     "general opening hours for the day of the week on which a public holiday occurs.

    See: https://schema.org/PublicHolidays
    Model depth: 5
    """

    type_: str = Field("PublicHolidays", const=True, alias="@type")


if TYPE_CHECKING:

    PublicHolidays.update_forward_refs()
