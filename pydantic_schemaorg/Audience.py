from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Audience(Intangible):
    """Intended audience for an item, i.e. the group for whom the item was created.

    See: https://schema.org/Audience
    Model depth: 3
    """
    type_: str = Field("Audience", alias='@type')
    audienceType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The target group associated with a given audience (e.g. veterans, car owners, musicians,"
     "etc.).",
    )
    geographicArea: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        None,
        description="The geographic area associated with the audience.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
