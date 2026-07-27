# ComicMetadataHub Source Capability Matrix

Version: 0.1
Status: Draft
Purpose:
Document available comic metadata sources,
their access methods, reliability, and intended use.

---

## Source Evaluation Criteria

| Capability | Meaning |
|---|---|
| API | Official programmatic access |
| JSON | Structured data embedded/exported |
| XML | Structured legacy format |
| CSV | Export/import capability |
| Scraping | HTML extraction possible |
| Authentication | Requires account/API key |
| Licensing | Data usage considerations |
| Priority | Development importance |

---

# Core Metadata Sources

## Comic Vine

| Field | Value |
|---|---|
| Source Type | Database API |
| API | Yes |
| JSON | Yes |
| XML | No |
| Authentication | API Key |
| Scraping Required | No |
| Primary Use | Issue metadata |
| Priority | Critical |

### Provides

- Publishers
- Series
- Issues
- Covers
- Creators
- Characters
- Locations
- Story arcs

### ComicMetadataHub Role

Primary metadata provider.

---

# ComicRack Compatibility

## ComicRack / Baerentsen Documentation

| Field | Value |
|---|---|
| Source Type | Documentation |
| API | No |
| JSON | No |
| XML | No |
| Scraping Required | No |
| Primary Use | Compatibility |
| Priority | Critical |

### Provides

- Field definitions
- Plugin behavior
- Scripting examples
- Metadata conventions

### ComicMetadataHub Role

Migration and compatibility reference.

---

# League of Comic Geeks

| Field | Value |
|---|---|
| Source Type | Community Database |
| API | Unknown |
| JSON | Unknown |
| XML | Unknown |
| Scraping Required | Possible |
| Authentication | Unknown |
| Primary Use | Collector metadata |
| Priority | High |

### Potential Data

- Series
- Issues
- Variants
- Covers
- Creators
- Collection information

### Investigation Needed

- Developer API availability
- Export options
- Rate limits
- Terms of service

---

# MyComicList

| Field | Value |
|---|---|
| Source Type | Web Database |
| API | Unknown |
| JSON | Unknown |
| XML | Unknown |
| Scraping Required | Possible |
| Primary Use | Secondary lookup |
| Priority | Medium |

### Potential Data

- Title discovery
- Issue listings
- Genre information

---

# IndyPlanet

| Field | Value |
|---|---|
| Source Type | Independent Publisher Marketplace |
| API | Unknown |
| JSON | Unknown |
| XML | Unknown |
| Scraping Required | Possible |
| Primary Use | Indie comics |
| Priority | Medium |

### Potential Data

- Creator-owned comics
- Small press titles
- Descriptions
- Cover images

---

# Future Sources

## Publisher Websites

Examples:

- Marvel
- DC
- Image
- Dark Horse
- IDW

Potential Uses:

- Verification
- Official release dates
- Creator credits

Priority:
Medium

---

# Source Priority Matrix

| Source | Metadata Value | Integration Difficulty | Priority |
|-|-|-|-|
| Comic Vine | Very High | Low | 1 |
| ComicRack | High | Low | 1 |
| League of Comic Geeks | High | Medium | 2 |
| IndyPlanet | Medium | Medium | 3 |
| MyComicList | Medium | Medium | 3 |
| Publisher Sites | High | High | 4 |

---

# Integration Rules

ComicMetadataHub should:

1. Prefer APIs over scraping.
2. Store source attribution.
3. Never overwrite conflicting metadata silently.
4. Preserve original source values.
5. Allow multiple metadata providers per field.
