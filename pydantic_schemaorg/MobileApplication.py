from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication


class MobileApplication(SoftwareApplication):
    """A software application designed specifically to work well on a mobile device such as"
     "a telephone.

    See: https://schema.org/MobileApplication
    Model depth: 4
    """
    type_: str = Field("MobileApplication", alias='@type')
    carrierRequirements: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Specifies specific carrier(s) requirements for the application (e.g. an application"
     "may only work on a specific carrier network).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
