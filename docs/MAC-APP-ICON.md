# Sales Command Dock icon

This small add-on connects to your existing installation. It does not change the website, browser database, speech model, pairing token, or contract files. No extra model or subscription is needed.

1. Stop the old launcher with **Control–C** in its Terminal window. Quit an existing Sales Command Dock launcher before replacing it.
2. Extract **Sales-Command-Mac-Icon.zip**. Double-click **install-mac-icon.command**. This one-time installation uses Terminal; everyday use does not.
3. In the folder picker, select the **existing Sales-Command folder you already use**, containing `dist` and `tools/.venv`. Do not select this small add-on folder.
4. Finder opens your personal **Applications** folder with **Sales Command.app** selected. Double-click it, then drag its icon into the Dock to keep it there.

Click the icon to start both the website and local transcription service and open **Safari at http://127.0.0.1:4173**. Keep using the same Safari profile that holds your saved data. Safari and the transcription helper run in the background without a Terminal window. Clicking again opens Safari without starting duplicate services.

**To stop:** right-click Sales Command in the Dock and choose **Quit**, or press Command–Q while Sales Command is the active app. Closing Safari alone leaves the services running. Quit after transcription has finished; quitting stops active processing too. A browser tab may remain open after quitting, but the local services stop. Saved browser data stays intact. This is not an automatic login/startup item.

Use normal **Quit**. Force Quit or an applet crash may leave background services running; reopen Sales Command and quit normally to stop them. The launcher requires the existing transcription installation to be ready before it opens Safari.

Keep the original Sales-Command folder in place: the icon points to it. If you move or rename that folder, reinstall the icon for the new location. A second hotel still uses the same app's property selector. Updating the website in the existing folder does not require replacing the icon.

If macOS blocks the downloaded installer, attempt to open it once, then use **System Settings → Privacy & Security → Open Anyway** for this installer and follow macOS's prompts. The app is built and locally signed on your Mac; it is not Apple-notarized. No Gatekeeper settings are disabled. If your work device prohibits local apps, follow your employer's device policy.

If ports 4173 or 8766 are busy, the app refuses to take over other processes. Stop the old Terminal launcher and try again. Logs are in `.local/launcher.log`, `.local/app.log`, and `.local/speech.log` inside the installed folder. If Call Desk asks for pairing again, open `tools/.speech-token` in TextEdit and paste it into Call Desk; do not share that token.

The icon installer uses only built-in macOS `osascript`, `osacompile`, and `codesign`, plus the existing speech helper's Python. It needs no administrator password or extra Python packages. Service lifecycle, duplicate-launch behavior, conflict handling, and installer construction are tested with local fixtures in Linux. Actual Finder/Dock/AppleScript compilation and Safari behavior must be confirmed on your Mac; they cannot be executed in this cloud workspace.
