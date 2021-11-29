from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalTest import MedicalTest


class PathologyTest(MedicalTest):
    """A medical test performed by a laboratory that typically involves examination of a tissue"
     "sample by a pathologist.

    See https://schema.org/PathologyTest.

    """

    tissueSample: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of tissue sample required for the test.",
    )
    locals().update({"@type": Field("PathologyTest", const=True)})


PathologyTest.update_forward_refs()
