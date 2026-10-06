from pathlib import Path
from pypdf import PdfReader
import json

root=Path(__file__).resolve().parent
assets=root/'dist/assets'
assets.mkdir(parents=True,exist_ok=True)
reader=PdfReader(r'E:\Users\Rahul kumar\Downloads\ALUMNI_MEET_26_With_SDG4_Logo.pdf')
names={'Image15.png':'sdg4.png','Image16.jpg':'srm-logo.jpg','Image17.jpg':'sdg17.jpg'}
for image in reader.pages[0].images:
    if image.name in names:
        (assets/names[image.name]).write_bytes(image.data)

init=root/'.superdesign/init'
init.mkdir(parents=True,exist_ok=True)
html=(root/'dist/index.html').read_text(encoding='utf-8')
css=(root/'dist/styles.css').read_text(encoding='utf-8')
files={
'components.md':'# Components\nBuildless vanilla HTML, CSS and JavaScript. No reusable component modules. Page-local buttons, native details and navigation are embedded in index.html.\n\n```html\n'+html+'\n```',
'layouts.md':'# Existing layout\nThe rejected version is a scrolling marketing-style page with an opening overlay. The approved replacement is a new seven-scene invitation-book flow, with no header navigation or marketing sections.\n\n```html\n'+html+'\n```',
'routes.md':'# Routes\n`/` is served from dist/index.html. Existing hash links address marketing sections. The replacement uses seven sequential invitation scenes on the same route. No framework, server, router or external component library.\n',
'theme.md':'# Tokens\nExisting paper #f5f1e8, ink #172a38, rust #98442d; DM Sans and Libre Caslon Display. Rejected landing-page aesthetic. Approved replacement: ivory #fffaf0, institutional blue #123d68, midnight #10263f, antique gold #b18a4a. Georgia-style readable serif, restrained ornament, invitations not website sections.\n\n```css\n'+css+'\n```',
'pages.md':'# Dependency tree\n- / : dist/index.html\n  - dist/styles.css\n  - dist/event-config.js\n  - dist/app.js\nNo recursive local imports. The approved new invitation replaces the existing landing page.\n',
'extractable-components.md':'# Extractable components\nNone. This is a single-purpose invitation, and the existing website shell is explicitly rejected. Do not extract its navigation, header or footer.\n'}
for name,text in files.items():(init/name).write_text(text,encoding='utf-8')
(root/'.superdesign/design-system.md').write_text('''# Reminisce’26 — Homecoming keepsake
One approved direction. Seven connected scenes: closed invitation, welcome-home message, formal event reveal, four presiding dignitaries, three faculty hosts, reunion-day programme, closing invitation.
Use warm ivory #fffaf0, institutional blue #123d68, midnight #10263f, antique gold #b18a4a. Serif Georgia display; Arial for small labels; normal text at least 16px on mobile. Real SRM, SDG4 and SDG17 assets extracted without alteration from the supplied PDF. Keep logos undistorted, on clean white/ivory supports with clear space.
Composition: one formal keepsake card on a dark textured background, fine double border and restrained engraved corners. No website navigation, marketing hero, feature cards or fabricated photos. Each scene continues from the previous with a shared gold line and paper-turn animation. All text remains live editable HTML. Only manual next/back, no auto advance; reduced motion supported.
Event: Reminisce'26, SRM Institute of Science and Technology (Deemed to be University), Tiruchirappalli, Faculty of Management. Saturday 17 October 2026, registration from 9:00 AM, programme ends 4:00 PM. Venue SRM Auditorium. No RSVP. Public link. Follow exact source PDF names, roles and all 16 programme items.
''',encoding='utf-8')
print(json.dumps({'assets':list(names.values()),'init':list(files)}))
