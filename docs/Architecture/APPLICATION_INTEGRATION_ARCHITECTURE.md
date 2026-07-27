# Application Integration Architecture

ComicMetadataHub is not a standalone comic management application.

ComicMetadataHub provides a metadata processing engine that is accessed through integrations/plugins for comic applications.

Supported integrations:

- ComicRack
- ComicTagger
- Future comic applications

Applications provide:

- User interface
- Comic selection
- Library navigation
- User commands

ComicMetadataHub provides:

- Metadata collection
- Metadata normalization
- Candidate discovery
- Candidate ranking
- Identity resolution
- Metadata merging
- Source attribution
- Conflict handling

---

# Integration Flow

The architecture is:

Comic Application

    |

Plugin / Integration Layer

    |

ComicMetadataHub Engine

    |

Metadata Sources

    |

ComicVine
GCD
Future Providers

    |

Matching / Resolving

    |

Canonical Metadata

    |

ComicInfo.xml Update

    |

Application Refresh

---

# ComicRack Workflow

Example:

User selects a comic in ComicRack.

User starts ComicMetadataHub automation.

ComicMetadataHub:

1. Reads existing comic metadata.
2. Normalizes the comic record.
3. Searches metadata sources.
4. Builds candidate matches.
5. Ranks candidates.
6. Resolves identity.
7. Applies metadata rules.
8. Updates ComicInfo.xml.

ComicRack can then refresh the comic metadata.

---

# ComicTagger Workflow

ComicTagger follows the same engine flow.

ComicTagger provides:

- Selected comic files
- Existing metadata
- User action

ComicMetadataHub provides:

- Metadata processing
- Matching
- Resolution
- Updated metadata

---

# Batch Processing

Batch processing is supported through the integrations.

Examples:

- ComicRack selecting multiple comics
- ComicTagger batch tagging

Batch rules:

High confidence:
- Apply automatically when configured.

Medium confidence:
- Require review.

Low confidence:
- Do not modify.

---

# Engine Responsibility

The engine must remain independent from any single application.

ComicRack and ComicTagger are clients of ComicMetadataHub.

They do not contain:

- matching logic
- provider logic
- merge rules

All metadata intelligence remains inside ComicMetadataHub.

