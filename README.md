# Reminisce’26 — Alumni homecoming invitation

This is a continuous digital invitation for SRM Tiruchirappalli alumni. Guests open a sealed envelope, watch the letter emerge, and scroll through a short reunion story. They untie a gold thread themselves to reveal the formal invitation and event details. The wording, event details, and authentic SRM/SDG marks came from the supplied invitation PDF. The wedding invitation shared by the requester informed the experience only; its design and assets were not reused.

The publishable site is in `dist/`. To change approved event information, edit `dist/event-config.js`; to change the invitation layout, edit `src/homecoming.template.html` and run `node build-invitation.cjs`. `dist/homecoming.css` and `dist/polish.css` supply the styling, while `dist/homecoming.js` controls the opening, music, countdown, calendar, sharing, and replay. The supplied reunion soundtrack is in `dist/assets/reminisce-reunion.mp3`.

The site includes no RSVP collection or invented contact information. It honors reduced-motion preferences and remains readable without JavaScript. The official logos are unchanged; the formal letter’s bright ivory field blends their white image backgrounds into the paper.

## GitHub Pages

The workflow in `.github/workflows/deploy-pages.yml` builds and publishes `dist/` from the `main` branch at [the public invitation](https://projectpk218.github.io/ALUMNI-MEET-INVITAION/). It uses that address for the Open Graph URL and preview image. The same static files are copied into the separate `SRM-MEETUP-INVITAION` repository connected to Netlify.
