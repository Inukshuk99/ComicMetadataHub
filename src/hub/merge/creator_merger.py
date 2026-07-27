"""
ComicMetadataHub Creator Merger

Merges creator information.
"""


class CreatorMerger:
    """
    Handles creator collection merging.
    """


    def merge(
        self,
        existing,
        incoming
    ):
        """
        Merge creator lists.
        """

        merged = list(
            existing
        )


        for creator in incoming:

            found = False


            for current in merged:

                if current.name == creator.name:

                    found = True


                    for role in creator.roles:

                        current.add_role(
                            role.role
                        )


                    break


            if not found:

                merged.append(
                    creator
                )


        return merged
