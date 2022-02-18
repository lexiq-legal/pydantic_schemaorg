from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest


class MedicalTestPanel(MedicalTest):
    """Any collection of tests commonly ordered together.

    See: https://schema.org/MedicalTestPanel
    Model depth: 4
    """
    type_: str = Field(default="MedicalTestPanel", alias='@type', const=True)
    subTest: Optional[Union[List[Union['MedicalTest', str]], 'MedicalTest', str]] = Field(
        default=None,
        description="A component test of the panel.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalTest import MedicalTest
