from pydantic import Field
from pydantic_schema_org.MedicalTest import MedicalTest
from typing import Any, Optional, Union, List


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
