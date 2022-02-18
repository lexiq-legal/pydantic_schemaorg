from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest


class PathologyTest(MedicalTest):
    """A medical test performed by a laboratory that typically involves examination of a tissue"
     "sample by a pathologist.

    See: https://schema.org/PathologyTest
    Model depth: 4
    """
    type_: str = Field(default="PathologyTest", alias='@type', const=True)
    tissueSample: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type of tissue sample required for the test.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
