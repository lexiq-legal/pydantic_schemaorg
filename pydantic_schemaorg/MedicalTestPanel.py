from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest
from typing import Any, Optional, Union, List


class MedicalTestPanel(MedicalTest):
    """Any collection of tests commonly ordered together.

    See https://schema.org/MedicalTestPanel.

    """
    type_: str = Field("MedicalTestPanel", const=True, alias='@type')
    subTest: Optional[Union[List[MedicalTest], MedicalTest]] = Field(
        None,
        description="A component test of the panel.",
    )
    

MedicalTestPanel.update_forward_refs()
