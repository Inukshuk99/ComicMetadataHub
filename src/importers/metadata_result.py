"""
ComicMetadataHub Metadata Result

Standard container returned by importers.
"""

from dataclasses import dataclass, field

from typing import Dict, Any, List


@dataclass
class MetadataResult:
    """
    Normalized raw metadata from an importer.
    """

    source: str

    success: bool = True

    data: Dict[str, Any] = field(
        default_factory=dict
    )

    warnings: List[str] = field(
        default_factory=list
    )

    errors: List[str] = field(
        default_factory=list
    )


    def add_warning(
        self,
        message: str
    ):
        self.warnings.append(
            message
        )


    def add_error(
        self,
        message: str
    ):
        self.errors.append(
            message
        )

        self.success = False