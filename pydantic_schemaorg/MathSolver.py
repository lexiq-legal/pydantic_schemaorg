from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class MathSolver(CreativeWork):
    """A math solver which is capable of solving a subset of mathematical problems.

    See: https://schema.org/MathSolver
    Model depth: 3
    """

    type_: str = Field("MathSolver", const=True, alias="@type")
    mathExpression: "Optional[Union[List[Union[str, SolveMathAction]], Union[str, SolveMathAction]]]" = Field(
        None,
        description="A mathematical expression (e.g. 'x^2-3x=0') that may be solved for a specific variable,"
        "simplified, or transformed. This can take many formats, e.g. LaTeX, Ascii-Math, or"
        "math as you would write with a keyboard.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.SolveMathAction import SolveMathAction

    MathSolver.update_forward_refs()
