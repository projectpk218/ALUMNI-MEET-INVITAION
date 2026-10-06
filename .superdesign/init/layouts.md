# Existing layout
The rejected version is a scrolling marketing-style page with an opening overlay. The approved replacement is a new seven-scene invitation-book flow, with no header navigation or marketing sections.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#172a38">
  <meta name="description" content="A personal invitation to reconnect with the people, ideas and institution that shaped your journey.">
  <title>Alumni Meet · A Personal Invitation</title>
  <link rel="stylesheet" href="styles.css">
  <script src="event-config.js" defer></script>
  <script src="app.js" defer></script>
</head>
<body>
<a class="skip-link" href="#invitation">Skip to invitation</a>
<div class="welcome" id="welcome" role="dialog" aria-modal="true" aria-labelledby="welcome-title" hidden>
  <div class="welcome-door left-door"></div><div class="welcome-door right-door"></div>
  <div class="welcome-top"><span data-event="institution">[INSTITUTION]</span><span>A personal invitation</span></div>
  <div class="welcome-content">
    <span class="eyebrow light">For the journeys that began here</span>
    <h1 id="welcome-title">Some journeys<br>bring us <em>back.</em></h1>
    <p id="guest-greeting">Dear alumnus, this invitation is for you.</p>
    <button class="button button-light" id="open-invitation">Open your invitation <span aria-hidden="true">↗</span></button>
    <span class="welcome-small">Old connections. New conversations.</span>
  </div>
  <svg class="welcome-art" viewBox="0 0 800 800" aria-hidden="true"><g fill="none" stroke="currentColor"><path d="M150 800V350a250 250 0 0 1 500 0v450M185 800V350a215 215 0 0 1 430 0v450M220 800V350a180 180 0 0 1 360 0v450M255 800V350a145 145 0 0 1 290 0v450"/><path d="M0 800L400 520L800 800M150 800L400 520L650 800M285 800L400 520L515 800M0 720H800M0 650H800M0 595H800"/></g><circle cx="400" cy="350" r="70" fill="currentColor" opacity=".1"/></svg>
  <div class="welcome-bottom"><span>One beginning. Many journeys.</span><button class="text-button" id="skip-opening">Skip opening <span aria-hidden="true">→</span></button></div>
</div>
<div id="site-shell">
<header class="site-header">
  <a class="institution" href="#invitation" aria-label="Back to invitation"><img id="official-logo" hidden alt=""><span data-event="institution">[INSTITUTION]</span></a>
  <nav aria-label="Main navigation"><a href="#the-gathering">The gathering</a><a href="#programme">Programme</a><a href="#venue">Venue</a><a class="nav-rsvp" href="#rsvp">RSVP <span aria-hidden="true">↗</span></a></nav>
  <button class="menu-toggle" id="menu-toggle" aria-expanded="false" aria-controls="mobile-menu">Menu <span aria-hidden="true">＋</span></button>
</header>
<nav id="mobile-menu" class="mobile-menu" aria-label="Mobile navigation" hidden><a href="#the-gathering">The gathering</a><a href="#programme">Programme</a><a href="#venue">Venue</a><a href="#rsvp">RSVP</a></nav>
<main id="invitation" tabindex="-1">
  <section class="hero section-wrap" aria-labelledby="event-title">
    <div class="hero-copy">
      <div class="eyebrow"><span class="small-line"></span> A gathering of our alumni</div>
      <p class="event-brand" id="event-title" data-event="brand">[EVENT_BRAND]</p>
      <h1>Back to where<br>it all <em>began.</em></h1>
      <p class="hero-description">Time has taken us in different directions.<br>Let’s come together for what comes next.</p>
      <a class="button" href="#rsvp">Reserve your place <span aria-hidden="true">↗</span></a>
      <a class="quiet-link" href="#the-gathering">Discover the gathering <span aria-hidden="true">↓</span></a>
    </div>
    <div class="hero-art" aria-label="Abstract architectural illustration of a shared beginning" role="img">
      <svg viewBox="0 0 600 720" aria-hidden="true">
        <defs><linearGradient id="arch-sky" x2="0" y2="1"><stop stop-color="#d5d7cf"/><stop offset="1" stop-color="#f0dbc2"/></linearGradient><linearGradient id="arch-floor" x2="0" y2="1"><stop stop-color="#dfc4a8"/><stop offset="1" stop-color="#b1947c"/></linearGradient><clipPath id="arch-window"><path d="M92 660V308a208 208 0 0 1 416 0v352Z"/></clipPath></defs>
        <path d="M44 682V302a256 256 0 0 1 512 0v380" fill="#e6d6c1"/>
        <path d="M66 682V302a234 234 0 0 1 468 0v380" fill="#cdb89d"/>
        <path d="M92 660V308a208 208 0 0 1 416 0v352Z" fill="url(#arch-sky)"/>
        <g clip-path="url(#arch-window)"><circle cx="346" cy="285" r="80" fill="#faf1d7"/><path d="M0 486Q120 441 237 477T600 460V720H0Z" fill="#b7bcb1"/><path d="M0 520Q165 482 296 516T600 494V720H0Z" fill="#8c9b94"/><path d="M278 512L102 720H562L323 512Z" fill="url(#arch-floor)"/><g stroke="#8c7765" stroke-width="1" opacity=".7"><path d="M294 512L232 720M309 512L410 720M238 560H379M209 598H421M171 648H480"/></g></g>
        <g stroke="#a68f73" fill="none"><path d="M22 682V302a278 278 0 0 1 556 0v380"/><path d="M44 682V302a256 256 0 0 1 512 0v380"/><path d="M66 682V302a234 234 0 0 1 468 0v380"/></g>
        <path d="M22 682H578L600 704H0Z" fill="#b5a087"/><path d="M0 704H600V720H0Z" fill="#d4bfa3"/>
      </svg>
      <img id="approved-hero" hidden alt="">
      <span class="art-caption"><span aria-hidden="true">✳</span> Shared roots. New horizons.</span>
      <span class="art-side-note">A return to connection</span>
    </div>
    <a class="scroll-cue" href="#the-gathering"><span>There’s more to the story</span><span aria-hidden="true">↓</span></a>
  </section>
  <section class="event-facts" aria-label="Event at a glance"><div><span class="eyebrow">When we gather</span><strong data-event="date">[EVENT_DATE]</strong><span><span data-event="time">[EVENT_TIME]</span> · <span data-event="timezone">[TIME_ZONE]</span></span></div><div><span class="eyebrow">Where we meet</span><strong data-event="venue" id="facts-venue">[VENUE_NAME]</strong><span data-event="mode">[EVENT_MODE]</span></div><div><span class="eyebrow">Our alumni community</span><strong data-event="cohort">[CLASS_YEARS_OR_COHORT]</strong><span>You are part of the story.</span></div></section>
  <section class="letter section-wrap" id="the-gathering">
    <div class="section-label"><span class="eyebrow">01 / The gathering</span><span class="asterisk" aria-hidden="true">✳</span></div>
    <div class="letter-copy reveal"><h2>A familiar beginning.<br><em>A new chapter.</em></h2><p class="lead">We may have left at different times.<br>We still share a place in each other’s story.</p><p>Join fellow alumni for <span data-event="brand">[EVENT_BRAND]</span> at <span data-event="institution">[INSTITUTION]</span>. A gathering to renew friendships, exchange perspectives, and celebrate the journeys that began with a shared experience.</p><p>Bring the stories you have collected and the person you have become. There is always more to discover when we come together.</p><div class="signature"><span class="signature-line"></span><div>With a warm welcome,<br><strong data-event="hosts">[HOSTS]</strong></div></div></div>
  </section>
  <section class="connection-band" aria-label="The spirit of the gathering"><span>Reconnect</span><i aria-hidden="true">✳</i><span>Reflect</span><i aria-hidden="true">✳</i><span>Reimagine</span></section>
  <section class="programme section-wrap" id="programme">
    <div class="programme-intro reveal"><span class="eyebrow">02 / Time well spent</span><h2>Good company.<br><em>Meaningful moments.</em></h2><p>A thoughtful gathering, shaped around the people and connections that matter.</p><div class="keynote"><span class="eyebrow">Featured voice</span><strong data-event="keynoteName">[KEYNOTE_NAME]</strong><span data-event="keynoteTitle">[KEYNOTE_TITLE]</span></div></div>
    <div class="agenda reveal"><div class="agenda-row"><span class="agenda-number">01</span><div><h3 data-agenda="0">[AGENDA_HIGHLIGHT_1]</h3><p>Programme details to be confirmed.</p></div><span class="agenda-mark" aria-hidden="true">↗</span></div><div class="agenda-row"><span class="agenda-number">02</span><div><h3 data-agenda="1">[AGENDA_HIGHLIGHT_2]</h3><p>Programme details to be confirmed.</p></div><span class="agenda-mark" aria-hidden="true">↗</span></div><div class="agenda-row"><span class="agenda-number">03</span><div><h3 data-agenda="2">[AGENDA_HIGHLIGHT_3]</h3><p>Programme details to be confirmed.</p></div><span class="agenda-mark" aria-hidden="true">↗</span></div><p class="agenda-footnote">Hosted by <span data-event="hosts">[HOSTS]</span></p></div>
  </section>
  <section class="countdown-section" aria-labelledby="countdown-title"><div class="section-wrap countdown-wrap"><div><span class="eyebrow light">Something to look forward to</span><h2 id="countdown-title">Until we meet <em>again.</em></h2><p id="countdown-caption">The countdown begins when the date is confirmed.</p></div><div class="countdown" id="countdown" aria-label="Event date to be confirmed"><div><strong data-count="days">—</strong><span>Days</span></div><div><strong data-count="hours">—</strong><span>Hours</span></div><div><strong data-count="minutes">—</strong><span>Minutes</span></div><div><strong data-count="seconds">—</strong><span>Seconds</span></div></div></div></section>
  <section class="venue section-wrap" id="venue"><div class="venue-visual reveal" aria-hidden="true"><div class="map-grid"></div><div class="map-ring ring-one"></div><div class="map-ring ring-two"></div><div class="map-ring ring-three"></div><div class="map-center">Here,<br><em>together.</em></div><span class="map-caption">A shared place. A shared moment.</span></div><div class="venue-copy reveal"><span class="eyebrow">03 / The meeting place</span><h2>Make your way<br><em>back to us.</em></h2><h3 data-event="venue" id="venue-name">[VENUE_NAME]</h3><p data-event="address" id="venue-address">[VENUE_ADDRESS]</p><a class="underlined-link" id="map-link" aria-disabled="true">View directions <span aria-hidden="true">↗</span></a><p class="small-note" id="map-note">The map will be available once the venue is confirmed.</p><div class="dress-note"><span class="eyebrow">Dress for the occasion</span><span data-event="dressCode">[DRESS_CODE]</span></div></div></section>
  <section class="rsvp-section" id="rsvp"><div class="rsvp-inner reveal"><span class="eyebrow">Your next chapter starts with a hello</span><h2>It wouldn’t be the same<br><em>without you.</em></h2><p>Some connections deserve more than a message.<br>We would love to see you again.</p><a class="button" id="rsvp-link" aria-disabled="true">RSVP opening soon <span aria-hidden="true">↗</span></a><p class="rsvp-deadline">Kindly respond by <span data-event="rsvpDeadline">[RSVP_DEADLINE]</span></p><p class="small-note" id="rsvp-note">Registration details are being finalised. No response has been collected.</p><div class="rsvp-extras"><button class="text-button" id="calendar-button" disabled>Add to calendar <span aria-hidden="true">＋</span></button><span aria-hidden="true">/</span><button class="text-button" id="share-button">Share invitation <span aria-hidden="true">↗</span></button></div><p id="action-message" class="small-note" role="status" aria-live="polite"></p></div><div class="rsvp-orbit" aria-hidden="true"></div></section>
  <section class="questions section-wrap"><div><span class="eyebrow">A few helpful details</span><h2>Before you <em>join us.</em></h2></div><div class="faq"><details><summary>Who is this gathering for?<span aria-hidden="true">＋</span></summary><p>This invitation is for the <span data-event="cohort">[CLASS_YEARS_OR_COHORT]</span> alumni community of <span data-event="institution">[INSTITUTION]</span>.</p></details><details><summary>What should I wear?<span aria-hidden="true">＋</span></summary><p>The dress code is <span data-event="dressCode">[DRESS_CODE]</span>. Final guidance will be updated here.</p></details><details><summary>How can I contact the organisers?<span aria-hidden="true">＋</span></summary><p><span data-event="contactName">[CONTACT_NAME]</span><br><a id="contact-email" data-event="contactEmail">[CONTACT_EMAIL]</a><br><a id="contact-phone" data-event="contactPhone">[CONTACT_PHONE]</a></p></details></div></section>
</main>
<footer class="site-footer"><div><span class="footer-brand" data-event="brand">[EVENT_BRAND]</span><p>One beginning. Many journeys.</p></div><div><span data-event="institution">[INSTITUTION]</span><p data-event="hashtag">[EVENT_HASHTAG]</p></div><a href="#invitation">Back to the beginning <span aria-hidden="true">↑</span></a></footer>
<div class="mobile-rsvp"><a href="#rsvp">Join the gathering <span aria-hidden="true">↗</span></a></div>
</div>
<noscript><style>.welcome{display:none!important}.reveal{opacity:1!important;transform:none!important}</style><p class="noscript-note">Enable JavaScript for the opening animation and live event details.</p></noscript>
</body></html>

```