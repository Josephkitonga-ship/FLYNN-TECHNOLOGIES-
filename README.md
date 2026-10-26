# Flynn Technologies website

Static multi-page site (HTML, CSS, JS). No build tools needed to host it.

## Before you launch
1. Open `build.py`, edit CONFIG (email, phone, location, domain, social links, form endpoint), then run `python3 build.py`.
2. Contact form: create a free form at formspree.io and paste its URL into `form_endpoint`.
3. Add images (missing ones show a branded placeholder automatically). Project screenshots are already included. Still needed:
   - `assets/gallery/01.jpg` ... `12.jpg` (order matches GALLERY list in build.py)
   - `assets/img/joseph-gitonga.jpg` (portrait) and `assets/img/og-image.png` (1200x630 share image)
4. Review case study text and the About story: drafts, edit to match what you delivered. Add real results/numbers.
5. Add Privacy Policy and Terms pages before running ads or collecting data.

## Deploy
Drag the folder onto Netlify, Cloudflare Pages or Vercel, then connect your domain.
