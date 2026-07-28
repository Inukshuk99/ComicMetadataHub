# ComicMetadataHub

**Universal Offline Comic Metadata Platform**

ComicMetadataHub is an open-source metadata engine designed to provide a single canonical metadata model for comic book collections.

It acts as a universal metadata hub between comic applications, metadata providers, and portable ComicInfo.xml files.

---

## Vision

ComicMetadataHub provides one consistent engine that can:

- Read and write ComicInfo.xml
- Merge metadata from multiple providers
- Maintain local metadata databases
- Keep metadata portable
- Operate offline whenever possible

---

## Supported Applications

Current:

- ComicRack CE
- ComicInfo.xml compatible applications

Providers:

- Comic Vine
- Grand Comics Database (GCD)

Planned:

- ComicTagger
- Additional community providers

---

## Core Design Goals

- Local-first architecture
- ComicInfo.xml as canonical metadata format
- Universal provider architecture
- KISS design
- Open source
- Community driven
- Extensible architecture

---

## Repository Structure

src/

    core/
    hub/
    importers/
        comicrack/

    exporters/
        comicrack/

    comicvine/
    gcd/
    services/
    updaters/

tests/

docs/

---

## Current Project Status

Foundation milestone complete.

Completed:

- ComicRack import pipeline
- ComicInfo.xml reader/writer
- Metadata mapping
- Matching engine
- Identity resolution
- Merge foundation
- ComicVine database layer
- GCD database layer
- Provider updater framework
- Repository cleanup

Testing:

- 51 tests passing

See:

- PROJECT_STATUS.md
- docs/MeetingNotes/SESSION_LOG.md

---

## Next Development Phase

- ComicVine API integration
- GCD integration
- CBR/RAR support
- Batch processing
- Production metadata workflows

---

## License

MIT License
