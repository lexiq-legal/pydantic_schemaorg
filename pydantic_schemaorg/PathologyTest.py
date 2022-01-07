from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.MedicalTest import MedicalTest


class PathologyTest(MedicalTest):
    """A medical test performed by a laboratory that typically involves examination of a tissue"
     "sample by a pathologist.

    See https://schema.org/PathologyTest.

    """
    type_: str = Field("PathologyTest", const=True, alias='@type')
    tissueSample: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of tissue sample required for the test.",
    )
    

PathologyTest.update_forward_refs()
