# Third-party components

Exact direct versions, declared licenses and repository addresses are in DEPENDENCIES.json. The lockfile pins npm artifacts and integrity values. npm package license files remain installed under node_modules. Keep required upstream notices when distributing.

Core additions: Dexie (Apache-2.0), Uppy (MIT), PDF.js (Apache-2.0), Tesseract.js (Apache-2.0), Mammoth (BSD-2-Clause), docx (MIT), Docxtemplater core (MIT/GPLv3 choice; this app uses the MIT option), PizZip (MIT/GPLv3 choice; MIT option), Signature Pad (MIT). Fonts distributed through Fontsource retain their upstream font licenses; Caveat, Allura, Great Vibes and Inter use SIL Open Font License terms. The npm English OCR-data package includes its own license and bundled model attribution.

Speech is an optional, separate Python component using native whisper.cpp (MIT) and a thin Python/PyAV audio bridge. See the installed Python distributions for their licenses. An official speech model is not bundled in this build. Model licensing and use requirements must be checked when downloading the selected model.

The original Sales Command handoff was supplied by the user; this work preserves its business logic and appearance. This application is not an official Hilton product and no vendor endorsement or private API entitlement is implied.
