from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class MathSolver(CreativeWork):
    """A math solver which is capable of solving a subset of mathematical problems.

    See https://schema.org/MathSolver.

    """
    type_: str = Field("MathSolver", const=True, alias='@type')
    mathExpression: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A mathematical expression (e.g. 'x^2-3x=0') that may be solved for a specific variable,"
     "simplified, or transformed. This can take many formats, e.g. LaTeX, Ascii-Math, or"
     "math as you would write with a keyboard.",
    )
    

MathSolver.update_forward_refs()
