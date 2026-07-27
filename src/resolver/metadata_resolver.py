"""
ComicMetadataHub Metadata Resolver

Matches imported metadata against
existing comic records.
"""


class ResolutionResult:
    """
    Result returned by the resolver.
    """


    def __init__(
        self,
        matched=False,
        score=0,
        reason=""
    ):

        self.matched = matched

        self.score = score

        self.reason = reason



class MetadataResolver:
    """
    Determines whether imported metadata
    matches existing records.
    """


    def resolve(
        self,
        incoming,
        existing
    ):
        """
        Compare incoming metadata
        against an existing record.
        """

        score = 0

        reasons = []


        # Identifier matching
        if (
            "identifier" in incoming
            and incoming["identifier"]
            ==
            existing.get("identifier")
        ):

            score += 100

            reasons.append(
                "Identifier match"
            )


        # Title matching
        if (
            incoming.get("title")
            ==
            existing.get("title")
        ):

            score += 40

            reasons.append(
                "Title match"
            )


        # Issue matching
        if (
            incoming.get("issue")
            ==
            existing.get("issue")
        ):

            score += 40

            reasons.append(
                "Issue match"
            )


        if score >= 100:

            return ResolutionResult(
                True,
                score,
                ", ".join(reasons)
            )


        return ResolutionResult(
            False,
            score,
            ", ".join(reasons)
        )