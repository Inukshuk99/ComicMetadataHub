# ComicMetadataHub Project State

Version: 0.1
Status: Active Development

---

# Project Purpose

ComicMetadataHub is a metadata normalization system.

It collects metadata from multiple sources, compares and resolves identities, stores canonical metadata, and exports compatible metadata for comic applications.

Supported goals:

- ComicRack compatibility
- ComicTagger compatibility
- CBZ/CBR/PDF workflows
- Multiple metadata providers
- Variant covers
- Printings
- Independent comics
- Future comic applications

---

# Current Git Checkpoints

## Completed Provider Architecture

Commit:

50b5a7aebd99dd09272f7ecdd180a92bb1766c4d

Completed:

- ComicVine database layer
- GCD database layer
- Provider database storage
- ComicVine updater
- GCD updater
- Updater framework
- Database updater
- Provider database tests

---

## Current Development Snapshot

Commit:

17334f83b4c33c29cb5223b0a384ea5dda31ac4e

Contains:

- Matching framework
- Candidate finder
- Candidate ranker
- Identity resolver
- Match pipeline
- Import pipeline foundations
- Matching tests

---

# Architecture Rules

## Metadata Ownership

ComicMetadataHub is the source of truth.

External applications consume exported metadata.

Sources:

- ComicVine
- GCD
- ComicRack
- Future providers

are metadata contributors.

They are not the final authority.

---

# Import Pipeline

The pipeline is:

External Source

    |

Data Collection

    |

Metadata Normalization

    |

Matching and Resolving

    |

Storage

    |

Export

---

# Matching Architecture

## Candidate Finder

Purpose:

Discover possible matches.

Should:

- collect candidates
- preserve source attribution
- avoid final decisions

Should NOT:

- select the winner
- remove valid alternatives too early

---

## Candidate Ranker

Purpose:

Score possible candidates.

Should compare:

- title
- series
- issue
- volume
- publisher
- year
- identifiers
- creators
- cover/image information
- provider confidence

---

## Identity Resolver

Purpose:

Determine whether two records represent the same comic.

Uses:

- identifiers
- metadata comparison
- confidence scoring

---

## Metadata Merger

Purpose:

Combine trusted metadata.

Rules:

- preserve source attribution
- never silently overwrite conflicts
- allow multiple providers per field

---

# Current Known Issue

Matching layer needs alignment.

Current problem:

CandidateFinder is filtering too aggressively.

Current flow:

CandidateFinder
    |
    v
CandidateRanker
    |
    v
IdentityResolver

Desired flow:

CandidateFinder
    |
    v
CandidateRanker
    |
    v
IdentityResolver

but with CandidateFinder discovering broader candidate sets.

---

# Development Rules

Before major changes:

1. Create Git checkpoint.
2. Change one architecture layer.
3. Run full test suite.
4. Commit passing state.

Do not:

- rewrite multiple layers without testing
- change architecture to satisfy a single test
- remove provider information
- lose source attribution

---

# Current Priority

Fix matching architecture while preserving:

- provider databases
- metadata model
- conflict handling
- source attribution

