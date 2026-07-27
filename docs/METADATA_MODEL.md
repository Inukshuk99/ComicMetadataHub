# ComicMetadataHub Metadata Model

Version: 0.2  
Status: Draft  
Sprint: 1  

## Purpose

Define the canonical metadata structure used internally by ComicMetadataHub.

ComicMetadataHub is designed as a metadata normalization system that can collect, compare, organize, and export comic metadata from multiple sources.

The system must support:

- ComicRack compatibility
- ComicTagger compatibility
- CBZ/CBR/PDF workflows
- Multiple metadata providers
- Different user folder organizations
- Variant covers
- Printings
- Independent comics
- Future comic applications

---

# 1. Core Design Principles

## Metadata Ownership

ComicMetadataHub is the source of truth for metadata.

External applications consume exported metadata.

Examples:

- ComicRack
- ComicTagger
- Kavita
- Komga
- Other comic readers

Relationship:
