from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest


class MedicalTestPanel(MedicalTest):
    """Any collection of tests commonly ordered together.

    See: https://schema.org/MedicalTestPanel
    Model depth: 4
    """
    type_: str = Field("MedicalTestPanel", alias='@type')
    subTest: Optional[Union[List[Union['MedicalTest', str]], 'MedicalTest', str]] = Field(
        None,
        description="A component test of the panel.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalTest import MedicalTest
