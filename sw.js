// Kutout offline cache: the page is always fetched fresh when online; everything else (AI model, library, icons) is kept after first use.
const V = 'kutout-v2';
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(
  caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim())
));
self.addEventListener('fetch', e => {
  const r = e.request, u = new URL(r.url);
  if (r.method !== 'GET' || u.origin !== location.origin) return;
  const isPage = r.mode === 'navigate' || /\/(index\.html)?$/.test(u.pathname);
  e.respondWith(isPage
    ? fetch(r).then(res => { const c = res.clone(); caches.open(V).then(x => x.put(r, c)); return res; })
        .catch(() => caches.match(r).then(h => h || caches.match('index.html')))
    : caches.match(r).then(h => h || fetch(r).then(res => { if (res.ok) { const c = res.clone(); caches.open(V).then(x => x.put(r, c)); } return res; })));
});
