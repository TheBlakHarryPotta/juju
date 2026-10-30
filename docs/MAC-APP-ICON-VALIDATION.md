# Mac launcher review

This is a standalone launcher add-on. It does not rebuild or replace the previously validated website release.

Passed `python tests/mac-launcher-tests.py`: **6 tests, zero failures**. These isolated Linux fixtures verify authenticated speech-health startup plus website availability, repeated starts reusing one supervisor, rejection of the wrong stop-instance identifier, socket mode 0600, normal shutdown, cleanup after termination, occupied ports left untouched, failed helper startup stopping the website, and a crashed helper's TERM-resistant child being stopped. Installer fixture checks compilation/signing command construction, paths containing spaces, model/token preservation, and refusal to overwrite an existing app. Compiler/signing commands are mocked in this installer fixture.

Also passed Python bytecode compilation and Bash syntax validation. The generated ICNS contains 16–1024 pixel PNG representations; the rendered bridge icon was visually checked.

Marcus implemented and inspected the launcher. The Breakers independently reviewed it, reproduced two descendant-cleanup failures in the first implementation, and confirmed the corrected cleanup and regression fixture. No blocking review findings remain.

Actual macOS AppleScript compilation, ad-hoc signing, Gatekeeper, Finder/Dock lifecycle, and Safari launch are **not tested in this Linux environment**. Normal Quit is the supported stop path. Force Quit can leave services running until the app is reopened and quit normally. No additional speech model, cloud processing, login item, administrator permission, or runtime package dependency is introduced.
