# whisper.cpp helper validation

Validated October 30, 2026. This change moves speech inference from the Python faster-whisper/CTranslate2 stack to the compiled `whisper-cli` executable. Python remains the local HTTP adapter; its inference dependency has been removed, and its requirement is `av==19.0.2` for bounded audio decoding.

## Results

| Check | Actual result |
|---|---|
| Native build | Aaron built the official whisper.cpp `v1.9.5` checkout at commit `d1be6fde11ac6e0407606b4e42fe72d34add8037` successfully on **Linux x86_64**, using GNU 14.2, CMake 4.4.4 and three build jobs. QA independently checked the checkout SHA and host architecture. |
| Executable startup | Aaron verified `whisper-cli --help` exits 0. The executable reports `1.9.5-dev` despite the pinned official `v1.9.5` tag. The executable is approximately 3.2 MB; this excludes shared libraries, source/build files and model weights. |
| Helper infrastructure | `tools/.venv/bin/python tests/speech-helper-tests.py -v`: **18 tests passed**, zero failures, in 4.477 seconds. |
| Browser compatibility | `SC_TEST_OUTPUT=test-results/whisper-ui npx playwright test tests/intake.spec.js tests/offline.spec.js -g 'manual call transcript\|production PWA'`: **2 tests passed**. Manual Call Desk transcript review commits a completed activity, and production offline reload still retains data and performs real local screenshot OCR. |
| Official model access | Aaron's request to `https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.en.bin` was blocked with an HTTP tunnel 403. No access policy or TLS verification was bypassed. No usable speech model was installed through that request. |
| Real speech recognition | **Not run.** The official JFK sample exists in the pinned source checkout, but actual inference requires the genuine model. No transcript accuracy, call performance or real-audio recognition success is claimed. |
| Apple Silicon / M1 | **Not built or benchmarked on M1 hardware.** A successful Linux build does not establish macOS installation, Metal execution, speed, temperature, power use or memory consumption. |

## What the 18 helper tests exercise

The tests start disposable loopback HTTP servers and use a clearly labeled synthetic `whisper-cli` fixture. The fixture validates the CLI arguments and normalized WAV shape, then writes predetermined JSON. **It does not recognize speech. Its text output is infrastructure evidence only.**

The tests verify:

- Pairing-token rejection, Origin restrictions, DNS-rebinding Host checks, approved CORS preflight and unknown endpoints.
- Missing executable, missing model and empty model report unavailable and refuse transcription. Mere file availability is distinguished from successful model execution through `modelValidated`.
- Upload content type, empty/invalid/oversized lengths, malformed audio and the 15-minute decoded-audio bound. PyAV actually converts the fixture audio to mono 16-bit 16 kHz PCM before the executable runs.
- Actual subprocess invocation and JSON-to-response conversion, plus executable failure, missing/oversized output, invalid JSON and invalid segment data.
- Actual subprocess timeout handling with the production subprocess budget reduced to 50 milliseconds **inside the test runner only**. The production 180-second deadline is unchanged; the test does not wait three minutes.
- Millisecond offsets, timestamp fallback, invalid/nonfinite time ranges, and empty results without invented speech.
- Request failure releases the transcription lock so another valid request can complete.

The parser test inputs and audio are synthetic. No confidential work audio, pairing credential or transcript was printed. Pairing material used by the tests is a disposable, predefined fixture value, separate from the real helper credential.

## Remaining verification

When authorized access to the official model becomes available, run the checked-in downloader with checksum verification intact, then test the official sample through both `whisper-cli` and the local HTTP adapter. Verify the genuine CLI JSON shape, transcript content, segment timing and model-validation health state. Test representative recordings separately; a known sample alone does not establish hotel-call accuracy.

The upstream model README gives SHA-1 `c78c86eb1a8faa21b369bcd33207cc90d64ae9df` for the selected `tiny.en` model; Aaron pinned that expected checksum in the downloader. A blocked download remains an external prerequisite, not a passing recognition test.

On the user's M1 Mac, separately verify the installer, native executable, Metal support and measured inference time/resource use. No M1 performance estimate is substituted for those measurements.

The earlier full application validation remains **40 passed, 1 explicitly skipped** as recorded in [VALIDATION.md](VALIDATION.md). The speech-helper change received the two relevant browser regression tests above; the unrelated full application suite was not rerun for this change.

## Final installer checks

The complete final `tools/setup-speech.sh` finished with exit code 0 after the Python 3.12+/NumPy requirements correction, reusing compiled native outputs. A fresh temporary virtual environment installed only the pinned PyAV and NumPy requirements and decoded/resampled the official JFK sample into 16 kHz mono PCM. This validates codec preprocessing, not inference. Checksum-negative tests rejected a mismatching downloaded model and removed its temporary file; an existing mismatching file was preserved unchanged. The real official model request remained blocked with HTTP 403 and left no partial model.
