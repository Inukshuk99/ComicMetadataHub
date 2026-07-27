# ComicMetadataHub Storage Architecture

Version: 0.1  
Status: Draft  
Sprint: 1

## Purpose

Define how ComicMetadataHub stores application files, configuration, metadata, cache files, and user library information.

The storage design must support:

- Multiple computers
- Large comic collections
- User-selected storage locations
- Backup and migration
- ComicRack compatibility
- ComicTagger compatibility

---

# 1. Storage Separation

ComicMetadataHub separates:

1. Application Files
2. Configuration Files
3. User Data
4. Export Data

---

# 2. Application Files

Application files contain only program components.

Example:
