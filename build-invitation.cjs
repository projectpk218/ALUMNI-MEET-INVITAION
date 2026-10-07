const fs = require('fs'), path = require('path'), vm = require('vm');
const root = __dirname;
const context = {window:{}};
vm.runInNewContext(fs.readFileSync(path.join(root,'dist/event-config.js'),'utf8'),context);
const event = context.window.ALUMNI_EVENT;
const escape = value => String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const person = p => `<div class="person"><h3>${escape(p.name)}</h3><p class="person-role">${escape(p.role)}</p><p class="person-institution">${escape(p.institution)}</p>${p.location?`<p class="person-location">${escape(p.location)}</p>`:''}</div>`;
const schedule = event.programme.map(([time,title])=>`<li><time>${escape(time)}</time><span>${escape(title)}</span></li>`).join('\n');
const strands = ['standing-left','standing-right','tail-left','tail-right','loop-left','loop-right','binding','crossing'].map(name => `<g class="cord-piece" data-cord="${name}"><use href="#cord-${name}" class="cord-edge"/><use href="#cord-${name}" class="cord-body"/><use href="#cord-${name}" class="cord-light"/><use href="#cord-${name}" class="cord-texture"/></g>`).join('\n');
const cord = fs.readFileSync(path.join(root,'src/cord-markup.html'),'utf8').replace('{{CORD_STRANDS}}', strands);
let html = fs.readFileSync(path.join(root,'src/homecoming.template.html'),'utf8').replace('{{CORD}}',cord).replace('{{LEADERSHIP}}',event.leadership.map(person).join('\n')).replace('{{HOSTS}}',event.hosts.map(person).join('\n'));
if (process.env.SITE_URL) {
  const site = new URL(process.env.SITE_URL);
  if (site.protocol !== 'https:' || site.username || site.password) throw Error('SITE_URL must be a public HTTPS URL');
  site.search = ''; site.hash = ''; site.pathname = site.pathname.replace(/\/$/, '') + '/';
  html = html.replace(/(<meta property="og:url" content=")[^"]+(">)/, (_, before, after) => before + escape(site.href) + after)
    .replace(/(<meta property="og:image" content=")[^"]+(">)/, (_, before, after) => before + escape(new URL('assets/reminisce-share.png', site).href) + after);
}
if (/\{\{[A-Z]+\}\}/.test(html)) throw Error('Unresolved source marker');
if (event.programme.length!==16 || event.leadership.length!==4 || event.hosts.length!==3) throw Error('Source count mismatch');
fs.writeFileSync(path.join(root,'dist/index.html'),html);
console.log('Homecoming invitation built: sealed letter, continuous illustrated flow, essential event details.');
