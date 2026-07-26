# ComicMetadataHub

**Universal Offline Comic Metadata Platform**

ComicMetadataHub is an open-source metadata engine designed to provide a **single canonical metadata model** for comic book collections.

Its purpose is to act as a universal metadata hub between comic management applications, online metadata providers, and portable ComicInfo.xml files.

---

## Vision

Instead of every application maintaining its own metadata workflow, ComicMetadataHub provides one consistent engine that can:

- Read and write ComicInfo.xml
- Merge metadata from multiple providers
- Store and maintain local metadata databases
- Keep metadata portable between applications
- Operate offline whenever possible

---

## Supported Applications (Planned)

- ComicRack CE
- ComicTagger
- Comic Vine
- Grand Comics Database (GCD)

Future providers may include:

- League of Comic Geeks
- Metron
- Additional community providers

---

## Core Design Goals

- ✅ Local-first architecture
- ✅ ComicInfo.xml as the canonical metadata format
- ✅ Universal provider architecture
- ✅ KISS (Keep It Simple)
- ✅ Open Source (MIT)
- ✅ Community driven
- ✅ Extensible plugin architecture

---

## Repository Structure

```
src/
    comicrack/
    comictagger/
    comicvine/
    gcd/
    hub/
    resolver/
    shared/

docs/
tests/
resources/
```

---

## Current Project Status

See:

- PROJECT_STATUS.md
- docs/MeetingNotes/SESSION_LOG.md

---

## License

MIT License
