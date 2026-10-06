# Alumni invitation website

An original, responsive invitation website built around a personal opening, editorial reunion story, event facts, programme, countdown, venue, RSVP and practical questions. The wedding invitation was used only to understand the experience, not as a visual template or source of code/assets.

The site is in `dist/`. Change approved event details in `dist/event-config.js`. No event facts, logos, photographs, dates, attendance figures or testimonials have been invented. The architectural illustration is abstract, not a depiction of a real institution. Replace it with approved photography through `heroImageUrl` and `heroImageAlt` if desired.

- Set `rsvpUrl` to the official registration page to activate RSVP. This site does not collect or store responses itself.
- Set `mapUrl` to enable directions.
- Supply `startISO` with an explicit time-zone offset to activate the countdown. Set `endISO` when known. Calendar export activates after the date and event name are supplied; no duration is invented.
- Enter valid contact details to activate email and phone links.
- Optional `?guest=Name` personalises the opening. The share button strips the guest name from shared URLs.
- Public joining credentials must be sent separately to confirmed attendees.
- Desktop and mobile navigation, reduced-motion preferences, keyboard controls and semantic document structure are supported.
- Google Fonts are optional: local Georgia and Arial fallbacks keep the website usable offline.

Deployment starts private for review. A private review URL cannot be used as a public invitation until sharing is explicitly changed. All bracketed placeholders must be replaced before inviting alumni.

The static `dist/` folder can also be deployed to a static host. No account, server or package installation is needed to edit the files locally.
