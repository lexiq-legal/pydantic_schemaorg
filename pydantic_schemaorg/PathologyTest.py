from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalTest import MedicalTest


class PathologyTest(MedicalTest):
    """A medical test performed by a laboratory that typically involves examination of a tissue"
     "sample by a pathologist.

    See: https://schema.org/PathologyTest
    Model depth: 4
    """

    type_: str = Field("PathologyTest", const=True, alias="@type")
    tissueSample: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The type of tissue sample required for the test.",
    )


if TYPE_CHECKING:

    PathologyTest.update_forward_refs()
