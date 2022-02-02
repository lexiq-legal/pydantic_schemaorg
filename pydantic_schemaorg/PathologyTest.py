from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest


class PathologyTest(MedicalTest):
    """A medical test performed by a laboratory that typically involves examination of a tissue"
     "sample by a pathologist.

    See: https://schema.org/PathologyTest
    Model depth: 4
    """
    type_: str = Field("PathologyTest", alias='@type')
    tissueSample: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The type of tissue sample required for the test.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
