from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest
from typing import Any, Union, List, Optional


class MedicalTestPanel(MedicalTest):
    """Any collection of tests commonly ordered together.

    See https://schema.org/MedicalTestPanel.

    """

    subTest: Optional[Union[List[MedicalTest], MedicalTest]] = Field(
        None,
        description="A component test of the panel.",
    )
    locals().update({"@type": Field("MedicalTestPanel", const=True)})


MedicalTestPanel.update_forward_refs()
