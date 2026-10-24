#!/usr/bin/env python3
"""Generates the Flynn Technologies multi-page site.
Edit CONFIG, run `python3 build.py`, and the .html files are rewritten."""
import os, datetime

# ============================ CONFIG — EDIT ME ============================
CONFIG = {
    "domain": "https://josephkitonga-ship.github.io/FLYNN-TECHNOLOGIES-",   # your live domain
    "email": "josephflynn774@gmail.com",          # public email
    "phone_display": "+254 742 258 137",               # shown on site
    "phone_intl": "254742258137",                      # digits only, for WhatsApp / tel links
    "location": "Kenya",                               # e.g. "Nairobi, Kenya"
    "form_endpoint": "https://formspree.io/f/YOUR_FORM_ID",  # from formspree.io
    "socials": {
        "Instagram": "https://instagram.com/",
        "LinkedIn": "https://linkedin.com/",
        "X": "https://x.com/",
        "Facebook": "https://facebook.com/",
        "TikTok": "https://tiktok.com/",
    },
}
# ==========================================================================

C = CONFIG
OUT = os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/%s?text=%s" % (C["phone_intl"], "Hello%20Director%20Flynn%2C%20I%20would%20like%20to%20discuss%20a%20new%20project.")

ICON = {
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 0 0-8.5 14.9L2 22l5.27-1.38A9.9 9.9 0 1 0 12.04 2Zm0 18.1a8.2 8.2 0 0 1-4.2-1.15l-.3-.18-3.13.82.84-3.05-.2-.31a8.2 8.2 0 1 1 7 3.87Zm4.5-6.1c-.25-.12-1.46-.72-1.69-.8-.23-.09-.39-.12-.56.12-.17.25-.64.8-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.38-1.72-.15-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.15.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.35-.77-1.85-.2-.48-.4-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.57.12.17 1.75 2.67 4.24 3.74.59.26 1.06.41 1.42.52.6.19 1.14.16 1.57.1.48-.07 1.46-.6 1.67-1.18.2-.58.2-1.07.14-1.18-.06-.1-.23-.17-.48-.29Z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" class="sun" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6"/></svg>',
 "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="moon" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/></svg>',
 "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "prev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg>',
 "next": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>',
}

NAV = [("index.html", "Base"), ("services.html", "Stack"), ("work.html", "Assets"),
       ("gallery.html", "Gallery"), ("about.html", "Director"), ("contact.html", "Direct access")]

def header(active):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active else "", t) for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="wrap hdr-in">
  <a class="brand" href="index.html" aria-label="Flynn Technologies home"><img src="assets/img/logo-mark.svg" alt="" width="36" height="36"><span class="brand-txt"><span class="brand-name">FLYNN</span><span class="brand-sub">Technologies</span></span></a>
  <nav class="nav" aria-label="Main">{links}</nav>
  <div class="hdr-actions"><button class="theme-btn" type="button" aria-label="Switch to light theme">{ICON["sun"]}{ICON["moon"]}</button><a class="btn btn-primary hdr-cta" href="contact.html">Brief the director</a></div>
</div></header>'''

def bottom_nav(active):
    cur = "work.html" if active == "gallery.html" else active
    P = {
     "index.html": '<img src="assets/img/logo-mark.svg" alt="" width="22" height="22">',
     "services.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 3 8l9 5 9-5-9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 16 9 5 9-5"/></svg>',
     "work.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/></svg>',
     "about.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
     "contact.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12Z"/></svg>',
    }
    tabs = "".join('<a href="%s"%s><span class="ic">%s</span><span>%s</span></a>' % (h, ' aria-current="page"' if h == cur else "", P[h], t) for h, t in NAV if h in P)
    return '<nav class="bnav" aria-label="Primary">%s</nav>' % tabs

def footer():
    soc = "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, n) for n, u in C["socials"].items())
    nav = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in NAV)
    return f'''<footer class="ftr"><div class="wrap">
  <div class="ftr-grid">
    <div><a class="brand" href="index.html"><img src="assets/img/logo-mark.svg" alt="" width="36" height="36"><span class="brand-txt"><span class="brand-name">FLYNN</span><span class="brand-sub">Technologies</span></span></a>
      <p class="ftr-about">Software engineering, AI automation and digital growth. Directed by Joseph Gitonga.</p></div>
    <div><h4>Explore</h4><ul>{nav}</ul></div>
    <div><h4>Follow</h4><ul>{soc}</ul></div>
    <div><h4>Direct access</h4><ul>
      <li><a href="mailto:{C["email"]}">{C["email"]}</a></li>
      <li><a href="tel:+{C["phone_intl"]}">{C["phone_display"]}</a></li>
      <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
      <li><span class="mute">{C["location"]}</span></li></ul></div>
  </div>
  <div class="ftr-base"><span>&copy; <span data-year>2026</span> Flynn Technologies. All rights reserved.</span><span><a href="privacy.html">Privacy</a> &middot; <a href="terms.html">Terms</a> &middot; Director: Joseph Gitonga</span></div>
</div></footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{ICON["wa"]}<span>Chat on WhatsApp</span></a>'''

def page(fname, title, desc, body, active, extra_head=""):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#05070D">
<link rel="canonical" href="{C["domain"]}/{fname if fname != "index.html" else ""}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Flynn Technologies">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{C["domain"]}/{fname if fname != "index.html" else ""}">
<meta property="og:image" content="{C["domain"]}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script>(function(){{var t="dark";try{{t=localStorage.getItem("flynn-theme")||"dark"}}catch(e){{}}var r=document.documentElement;r.setAttribute("data-theme",t==="light"?"light":"dark");r.classList.add("js")}})()</script>
<link rel="stylesheet" href="assets/css/style.css">
{extra_head}
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
{bottom_nav(active)}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)

# ------------------------------ helpers -----------------------------------
def shot(domain, variant, img):
    return f'''<div class="shot"><div class="shot-bar"><i></i><i></i><i></i><span>{domain}</span></div>
<div class="shot-body {variant}"><div class="ph" aria-hidden="true"><b></b><b></b><b></b><b></b><b></b></div>
<img src="assets/work/{img}" alt="Screenshot of {domain}" loading="lazy" onerror="this.remove()"></div></div>'''

def cta(title="Brief the director.", text="State the scope. Joseph Gitonga responds directly. Response SLA: one working day."):
    return f'''<section class="sec" aria-labelledby="cta-h"><div class="wrap"><div class="cta-box">
  <div><h2 id="cta-h">{title}</h2><p>{text}</p></div>
  <div class="cta-actions"><a class="btn btn-dark" href="contact.html">Open a brief</a><a class="btn btn-line-dark" href="{WA}" target="_blank" rel="noopener">WhatsApp the director</a></div>
</div></div></section>'''

# ------------------------------ HOME --------------------------------------
home_body = f'''
<section class="hero" aria-labelledby="hero-h">
  <div class="wrap hero-grid">
    <div>
      <h1 id="hero-h"><span class="rise" style="--i:0">Flynn Technologies builds platforms</span><span class="rise h-grow" style="--i:1">that run in production.</span></h1>
      <p class="lead hero-lead rise" style="--i:2">Storefronts that sell. Systems that run themselves. Growth you can measure. E-commerce platforms, mobile-first sites and automation for Kenyan businesses, designed, built and launched by one accountable director, from first brief to live site.</p>
      <div class="hero-cta rise" style="--i:3"><a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">Brief the director</a><a class="btn btn-ghost" href="work.html">Audit live assets</a></div>
    </div>
    <div class="planner rise" style="--i:4" data-planner data-wa="{C["phone_intl"]}">
      <h2>Scope your build</h2>
      <p class="mute">Select the scope. The brief goes straight to Director Flynn on WhatsApp.</p>
      <div class="opts-row" role="group" aria-label="What do you need?">
        <button class="chip" type="button" aria-pressed="false">Custom software</button>
        <button class="chip" type="button" aria-pressed="false">AI and automation</button>
        <button class="chip" type="button" aria-pressed="false">Digital growth</button>
        <button class="chip" type="button" aria-pressed="false">Full platform</button>
      </div>
      <a class="btn btn-primary" data-planner-send href="{WA}" target="_blank" rel="noopener">Send brief on WhatsApp</a>
      <p class="form-note">Response SLA: one working day.</p>
    </div>
  </div>
</section>

<section class="wrap" aria-label="Why Flynn"><ul class="strip">
  <li><strong>Mobile-first by default</strong><span class="mute">Built for the phone in your customer&rsquo;s hand.</span></li>
  <li><strong>Single-director execution</strong><span class="mute">One accountable engineer from brief to production.</span></li>
  <li><strong>Live platforms in service</strong><span class="mute">Real domains. Real customers. Open to inspection.</span></li>
</ul></section>

<section class="sec" aria-labelledby="pil-h"><div class="wrap">
  <div class="sec-head"><h2 id="pil-h">Three engineering domains.</h2></div>
  <div class="together">
    <article><h3>Custom software</h3><p class="mute">Front ends engineered for mobile networks and daily operation.</p><ul class="mini"><li>Storefronts and sites built for speed</li><li>Admin portals, inventory, order state</li><li>Installable progressive web apps</li></ul><a class="link" href="services.html#software">View the stack</a></article>
    <article><h3>AI and automation</h3><p class="mute">Automation that never clocks off.</p><ul class="mini"><li>Assistants trained on catalogue data</li><li>Branch-specific WhatsApp order routing</li><li>Inventory, reports and messages synced</li></ul><a class="link" href="services.html#automation">View automation specs</a></article>
    <article><h3>Digital growth</h3><p class="mute">Acquisition engineered for measurable revenue.</p><ul class="mini"><li>Social distribution and content ops</li><li>Technical SEO and paid campaigns</li><li>Brand identity and positioning</li></ul><a class="link" href="services.html#growth">View growth specs</a></article>
  </div>
</div></section>

<section class="sec" aria-labelledby="build-h"><div class="wrap">
  <div class="sec-head"><h2 id="build-h">From static site to full commerce platform.</h2><p class="lead">Each tier ships production-ready and scales into the next without a rebuild.</p></div>
  <div class="together four sw">
    <article><h3>Business websites</h3><p class="mute">Static pages on a global CDN. Instant loads, structured data, lead capture.</p></article>
    <article><h3>Online stores</h3><p class="mute">Catalogue, cart and M-Pesa STK Push checkout. Admin console for products, stock and order state.</p></article>
    <article><h3>E-commerce platforms</h3><p class="mute">Multi-branch catalogues on Cloudflare D1 or Supabase. Accounts, delivery rules, reporting, API integrations.</p></article>
    <article><h3>Custom web and mobile apps</h3><p class="mute">Booking, membership, logistics and internal systems on serverless Workers back ends.</p><a class="link" href="services.html#software">Review the full stack</a></article>
  </div>
</div></section>

<section class="sec" aria-labelledby="who-h"><div class="wrap split-2">
  <figure class="photo"><img src="assets/img/ops-engineer.jpg" alt="Engineer reviewing plans on screens and paper in a control room" loading="lazy" onerror="this.remove()"></figure>
  <div>
    <h2 id="who-h">Deployed across commercial sectors.</h2>
    <p class="lead" style="margin-top:1rem">From single-outlet shops to multi-branch operations, Director Flynn specifies only what the operation requires. Every build is mobile-first, performance-budgeted and designed around how customers actually buy.</p>
    <ul class="checklist">
      <li><strong>Retail and fashion</strong><span class="mute">Catalogues and full e-commerce: STK Push checkout, stock control, delivery rules.</span></li>
      <li><strong>Sports and leisure</strong><span class="mute">Shops, bookings, memberships. Sale pricing, wishlists, customer accounts.</span></li>
      <li><strong>Wholesale and distribution</strong><span class="mute">Stock, orders and multi-branch dashboards in one operating portal.</span></li>
      <li><strong>Hospitality and travel</strong><span class="mute">Room and table enquiries, media galleries, booking requests routed to the manager.</span></li>
      <li><strong>Transport and logistics</strong><span class="mute">Digital manifests, parcel tracking, reservations.</span></li>
      <li><strong>Professional services</strong><span class="mute">Credible web presence, lead capture, local search visibility.</span></li>
    </ul>
  </div>
</div></section>

<section class="sec sec--alt" aria-labelledby="work-h"><div class="wrap">
  <div class="sec-head"><h2 id="work-h">Production assets. Live and auditable.</h2><p class="lead">Two Kenyan e-commerce platforms in service. Mobile-first, performance-budgeted, open to inspection.</p></div>
  <div class="works">
    <a class="work" href="work-maggies-collection.html">{shot("maggiescollection.co.ke", "v1", "maggies-collection.jpg")}
      <div class="work-meta"><h3>Maggie&rsquo;s Collection</h3><p class="mute">Family fashion retail, Kimana Town. Catalogue, size guide, holds and local delivery.</p><ul class="tags"><li>Storefront</li><li>Commerce</li></ul><span class="link">Open the audit</span></div></a>
    <a class="work" href="work-baari-sports-centre.html">{shot("baarisportscentre.co.ke", "v2", "baari-sports-centre.jpg")}
      <div class="work-meta"><h3>Baari Sports Centre</h3><p class="mute">Sports retail platform. Category navigation, sale pricing, cart and live chat.</p><ul class="tags"><li>Storefront</li><li>Commerce</li></ul><span class="link">Open the audit</span></div></a>
  </div>
</div></section>

<section class="sec sec--alt" aria-labelledby="gets-h"><div class="wrap">
  <div class="sec-head"><h2 id="gets-h">Standard on every deployment</h2><p class="lead">Baseline specification. No line items, no upsell.</p></div>
  <ul class="gets">
    <li><h3>Mobile-first design</h3><p>Designed on a phone screen first, then scaled up.</p></li>
    <li><h3>Direct contact paths</h3><p>Call, WhatsApp and form access from every page.</p></li>
    <li><h3>Search-ready markup</h3><p>Titles, meta, sitemap and structured data on every route.</p></li>
    <li><h3>Built for speed</h3><p>Compressed images and lean code, tuned for slow connections.</p></li>
    <li><h3>Analytics</h3><p>Traffic, page-level behaviour and conversion events tracked.</p></li>
    <li><h3>Operator-editable content</h3><p>Text, photos and prices change without a deployment.</p></li>
    <li><h3>Secure hosting</h3><p>HTTPS, backups and domain configuration documented.</p></li>
    <li><h3>Training and handover</h3><p>Documented walkthrough before the system passes to the operator.</p></li>
  </ul>
</div></section>

<section class="sec" aria-labelledby="proc-h"><div class="wrap" data-hscroll>
  <div class="head-row"><div class="sec-head" style="margin-bottom:0"><h2 id="proc-h">Delivery sequence</h2><p class="lead">Five phases. Fixed order. Defined outputs.</p></div>
    <div class="hs-ctrl"><button class="icon-btn" type="button" data-hs="-1" aria-label="Previous step">{ICON["prev"]}</button><button class="icon-btn" type="button" data-hs="1" aria-label="Next step">{ICON["next"]}</button></div></div>
  <ol class="hscroll" tabindex="0" aria-label="Project steps, scroll sideways"><li class="gcard"><span class="n" aria-hidden="true">1</span><h3>Discover</h3><p>Director Flynn audits operations, customers and success metrics.</p></li><li class="gcard"><span class="n" aria-hidden="true">2</span><h3>Plan</h3><p>Written scope, timeline and price. Nothing starts without sign-off.</p></li><li class="gcard"><span class="n" aria-hidden="true">3</span><h3>Build</h3><p>Staged delivery. Each stage reviewed and approved before the next.</p></li><li class="gcard"><span class="n" aria-hidden="true">4</span><h3>Launch</h3><p>Tested on real devices and networks, then deployed to production.</p></li><li class="gcard"><span class="n" aria-hidden="true">5</span><h3>Grow</h3><p>Reporting, optimisation and marketing against measured targets.</p></li></ol>
</div></section>
<section class="sec" aria-labelledby="hfaq-h"><div class="wrap">
  <div class="sec-head"><h2 id="hfaq-h">Direct answers</h2></div>
  <div class="faq">
    <details><summary>How long does a project take?</summary><p>Business sites: three to six weeks. Commerce platforms, apps and custom systems: scoped per build, with a fixed timeline in the written plan.</p></details>
    <details><summary>What does it cost?</summary><p>Priced per scope. After a short call, a written quote itemises every deliverable. Marketing runs on a monthly retainer.</p></details>
    <details><summary>Are software and marketing sold together?</summary><p>No. Each runs independently. Combined engagements share one plan, one data layer and one point of accountability.</p></details>
    <details><summary>Can you build a full e-commerce platform?</summary><p>Yes. Product management, secure checkout, M-Pesa Daraja STK Push with callback reconciliation, stock tracking, delivery rules and an admin dashboard on Cloudflare D1 or Supabase. Branch-specific WhatsApp order routing is available.</p></details>
  </div>
  <p style="margin-top:1.5rem"><a class="link" href="services.html#faq-h">Open the full FAQ</a></p>
</div></section>
{cta()}
'''
org_ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context":"https://schema.org","@type":"ProfessionalService","name":"Flynn Technologies","url":C["domain"],"logo":C["domain"]+"/assets/img/logo-mark.svg","image":C["domain"]+"/assets/img/og-image.png","email":C["email"],"telephone":"+"+C["phone_intl"],"areaServed":"Kenya","founder":{"@type":"Person","name":"Joseph Gitonga"},"description":"Custom software, AI automation and digital marketing for businesses in Kenya.","serviceType":["Custom software development","Website and online shop development","AI and business automation","Social media marketing","SEO and digital advertising"]}) + '</script>'
page("index.html", "Flynn Technologies | Director Joseph Gitonga: software, AI automation, commerce",
     "Flynn Technologies builds custom software, automates repetitive work with AI, builds websites and online stores, and runs the digital marketing that grows your business in Kenya.",
     home_body, "index.html", org_ld)

# ------------------------------ SERVICES ----------------------------------
def rows(items):
    return '<div class="rows">' + "".join(f'<div class="row"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + "</div>"

software = [
 ("Business websites", "Professional mobile-first sites, from a few simple pages to larger company sites, with contact forms and a search-friendly setup. Best for new and established businesses that want to be found and trusted."),
 ("Online stores and e-commerce platforms", "Catalogue, cart, secure checkout, M-Pesa and other online payments, stock and order management, delivery options and an admin dashboard. From a small shop to a large multi-category platform."),
 ("Web and mobile apps", "Installable apps that run on any phone or computer with no app-store delays. Best for bookings, memberships and customer portals."),
 ("Admin portals and stock systems", "Manage products, orders, staff and branches from one simple dashboard. Best for shops with more than one counter or location."),
 ("Integrations", "Connect M-Pesa payments, messaging, maps and the tools you already use, so data moves without retyping."),
 ("Support and updates", "Hosting, security updates, backups and improvements after launch, so nothing goes stale."),
]
automation = [
 ("Customer assistants", "Chat assistants that answer common questions about products, sizes, prices and delivery at any hour, then pass real orders to your team."),
 ("Order and enquiry routing", "Send orders, bookings and enquiries to the right person or branch automatically, by WhatsApp, SMS or email, so nothing waits in an inbox."),
 ("Workflow automation", "Keep inventory, reports and customer messages in sync without copying data by hand."),
]
growth = [
 ("Social media management", "A posting plan, designed posts and replies to your community, every week, on the platforms your customers use."),
 ("Content and creative", "Product photography direction, short videos, graphics and captions that sound like your brand."),
 ("Paid ads", "Facebook, Instagram, TikTok and Google campaigns with a budget you control and results you can read."),
 ("SEO", "Make your site easier to find when people search for what you sell, including local searches in your town."),
 ("Branding", "Logo, colours and voice, so every post and page looks like one business."),
 ("Reporting", "A plain monthly report: what worked, what did not, and what we change next."),
]
packages_html = """
<section class="sec" aria-labelledby="pk-h"><div class="wrap">
  <div class="sec-head"><h2 id="pk-h">Four ways to start</h2><p class="lead">Every project is quoted to fit your business. These are the usual starting points, and each one can grow into the next.</p></div>
  <div class="together four">
    <article><h3>Online presence</h3><p class="mute">A professional website that gets you found.</p><ul class="mini"><li>Mobile-first business website</li><li>Contact form, call and map buttons</li><li>Basic SEO and sharing previews</li><li>Training and handover</li></ul><p class="mute" style="font-size:.92rem">Best for new and small businesses.</p><a class="link" href="contact.html">Get a quote</a></article>
    <article><h3>Online store</h3><p class="mute">Sell products online with a complete shopping experience.</p><ul class="mini"><li>Catalogue with categories and prices</li><li>Cart and secure checkout</li><li>M-Pesa and other payment options</li><li>Admin to manage products, stock and orders</li></ul><p class="mute" style="font-size:.92rem">Best for fashion, sports and retail shops.</p><a class="link" href="contact.html">Get a quote</a></article>
    <article><h3>E-commerce platform</h3><p class="mute">A full platform for larger or growing operations.</p><ul class="mini"><li>Multi-category and multi-branch catalogues</li><li>Customer accounts and order history</li><li>Stock, delivery and reporting tools</li><li>Integrations with your existing systems</li></ul><p class="mute" style="font-size:.92rem">Best for wholesalers, marketplaces and chains.</p><a class="link" href="contact.html">Get a quote</a></article>
    <article><h3>Growth partner</h3><p class="mute">Keep customers coming every month.</p><ul class="mini"><li>Social media planning and content</li><li>Ad campaigns and SEO updates</li><li>Monthly performance report</li><li>Website support and updates</li></ul><p class="mute" style="font-size:.92rem">Best for businesses that already have a site.</p><a class="link" href="contact.html">Get a quote</a></article>
  </div>
</div></section>
"""
faqs = [
 ("How long does a website take?", "A typical business website takes three to six weeks from the first call to launch. Apps and custom systems take longer, and we give you a timeline in the plan before you commit."),
 ("How much does a project cost?", "It depends on the scope. After a short call we send a written quote with what is included, so there are no surprises. Marketing is billed monthly."),
 ("Is AI right for my business?", "Sometimes. We start by looking at which tasks repeat every day, such as answering the same questions or copying orders, and tell you honestly whether automation will save you time."),
 ("Can I update the website myself?", "Yes. We build sites so you can change text, photos and prices without a developer, and we show you how during handover."),
 ("Do I own my website?", "Yes. Your domain, content and website belong to you. We hand over the accounts and files when the project is complete."),
 ("Can you work with my existing website?", "Yes. We can redesign it, add features such as online payments, booking or stock management, or take over its updates and marketing."),
 ("Do you work outside my town?", "Yes. We work across Kenya, and most of the work happens by WhatsApp, phone and video call."),
 ("What happens after launch?", "We stay available. You can add a support plan for hosting, updates and fixes, or hand over everything and manage it yourself."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
def svc(sid, h, lead, accent, items, btn, alt=False):
    return f'''<section class="sec{" sec--alt" if alt else ""}" id="{sid}" aria-labelledby="{sid}-h"><div class="wrap svc" style="--accent:{accent}">
  <div class="svc-head"><span class="bar-accent"></span><h2 id="{sid}-h">{h}</h2><p class="lead">{lead}</p><div>{btn}</div></div>
  {rows(items)}
</div></section>'''
services_body = f'''
<section class="phero"><div class="wrap"><h1>One team to build it, automate it and grow it.</h1>
  <p class="lead">Use any service on its own, or combine them. Everything is planned around your customers and your phone-first market.</p>
  <div class="hero-cta"><a class="btn btn-blue" href="#software">Software</a><a class="btn btn-ghost" href="#automation">AI and automation</a><a class="btn btn-orange" href="#growth">Digital growth</a></div></div></section>
{svc("software", "Custom software", "We design, build and look after the software your business and customers use.", "var(--blue-2)", software, '<a class="btn btn-blue" href="contact.html">Ask about software</a>')}
{svc("automation", "AI and automation", "Take repetitive work off your team and keep serving customers when the shop is closed.", "var(--cyan)", automation, '<a class="btn btn-ghost" href="contact.html">Ask about automation</a>', True)}
{svc("growth", "Digital growth", "We help people find your business, remember it and choose it.", "var(--orange)", growth, '<a class="btn btn-orange" href="contact.html">Ask about marketing</a>')}
{packages_html}
<section class="sec sec--light" aria-labelledby="faq-h"><div class="wrap">
  <div class="sec-head"><h2 id="faq-h">Questions we hear often</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>
{cta("Not sure what you need?", "Describe your business in a message and we will suggest where to start.")}
'''
faq_ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in faqs]}) + '</script>'
page("services.html", "Services | Flynn Technologies",
     "Custom software, AI and automation, and digital marketing from one team: websites, e-commerce platforms, apps, automation, social media, ads and SEO.",
     services_body, "services.html", faq_ld)

# ------------------------------ WORK --------------------------------------
work_body = f'''
<section class="phero"><div class="wrap"><h1>Live work you can visit.</h1>
  <p class="lead">Two Kenyan online shops. Open a case study to see the problem, what we built and what customers can now do.</p></div></section>
<section class="sec" style="padding-top:1rem"><div class="wrap">
  <div class="works">
    <a class="work" href="work-maggies-collection.html">{shot("maggiescollection.co.ke", "v1", "maggies-collection.jpg")}
      <div class="work-meta"><h3>Maggie&rsquo;s Collection</h3><p class="mute">A family fashion store in Kimana Town, online with a catalogue, size guide, holds and local delivery.</p><ul class="tags"><li>Web design</li><li>Development</li></ul><span class="link">Read the case study</span></div></a>
    <a class="work" href="work-baari-sports-centre.html">{shot("baarisportscentre.co.ke", "v2", "baari-sports-centre.jpg")}
      <div class="work-meta"><h3>Baari Sports Centre</h3><p class="mute">A sports shop online, with categories, sale prices, a cart and a live chat button.</p><ul class="tags"><li>Web design</li><li>Development</li></ul><span class="link">Read the case study</span></div></a>
  </div>
  <p style="margin-top:2rem"><a class="link" href="gallery.html">Browse the project gallery</a></p>
  <div class="work-cta" style="margin-top:2rem"><h3>Your project could be next.</h3><p class="mute">We are taking on new software, automation and marketing work.</p><a class="btn btn-primary" href="contact.html">Start a project</a></div>
</div></section>
'''
page("work.html", "Work | Flynn Technologies",
     "Case studies from Flynn Technologies: Maggie's Collection and Baari Sports Centre, two live Kenyan online shops.", work_body, "work.html")

def case(fname, name, domain, img, oneliner, challenge, built, results, other, other_h, services):
    built_li = "".join(f"<li>{b}</li>" for b in built)
    res_li = "".join(f"<li>{r}</li>" for r in results)
    body = f'''
<section class="phero"><div class="wrap"><h1>{name}</h1><p class="lead">{oneliner}</p>
  <dl class="facts"><div><dt>Client</dt><dd>{name}</dd></div><div><dt>Live website</dt><dd><a class="link" href="https://{domain}" target="_blank" rel="noopener">{domain}</a></dd></div><div><dt>What we did</dt><dd>{services}</dd></div></dl></div></section>
<section class="sec" style="padding-top:1rem"><div class="wrap case-layout">
  <div class="phone-wrap"><div class="phone"><img src="assets/work/{img}" alt="{name} website on a phone" width="720"></div>
    <a class="btn btn-ghost" href="https://{domain}" target="_blank" rel="noopener">Visit the live site</a></div>
  <div>
    <div class="case"><h2>The challenge</h2><div class="measure">{challenge}</div></div>
    <div class="case"><h2>What we built</h2><ul class="ticks">{built_li}</ul></div>
    <div class="case"><h2>What customers can now do</h2><ul class="ticks">{res_li}</ul></div>
    <div class="next"><span class="mute">Next case study</span><a class="big" href="{other}">{other_h}</a></div>
  </div>
</div></section>
{cta()}'''
    page(fname, f"{name} case study | Flynn Technologies", oneliner, body, "work.html")

case("work-maggies-collection.html", "Maggie\u2019s Collection", "maggiescollection.co.ke", "maggies-collection.jpg",
     "A family fashion store in Kimana Town, online with a catalogue, size guide, holds and local delivery.",
     "<p>Maggie&rsquo;s Collection has been selling quality clothes for men, women and kids in Kimana Town since 2020. The shop needed an online home that shows what is on the rails, makes sizes and prices clear, and lets a customer reach the shop in one step.</p>",
     ["A warm, editorial storefront with a clear headline, a photo of the real shop and two main actions: browse the rails or find your size", "Women, men and kids sections side by side, so a whole family can shop in one visit", "A &ldquo;New on the rail&rdquo; carousel with prices, discount badges and size or option pickers on each product", "Catalogue, Delivery and Holds, and Size Guide pages in the main menu", "An &ldquo;Ask the concierge&rdquo; help button that stays on screen as customers browse"],
     ["Pick items for the whole family and send one WhatsApp message to hold them", "Arrange local delivery to town without calling the shop", "See the price, the discount and the available sizes before they ask", "Browse comfortably on a phone, with a layout designed for small screens"],
     "work-baari-sports-centre.html", "Baari Sports Centre", "Web design and development")
case("work-baari-sports-centre.html", "Baari Sports Centre", "baarisportscentre.co.ke", "baari-sports-centre.jpg",
     "A sports shop online, with categories, sale prices, a cart and a live chat button.",
     "<p>Baari Sports Centre sells football boots, jerseys and accessories. Its customers needed to scan a lot of products quickly on a phone, spot the deals and buy without friction.</p>",
     ["A bold dark design with a lime accent that matches the energy of sport", "Category tabs for All, Boots, Jerseys, Accessories and Training, so shoppers jump straight to what they want", "Product cards with sale badges, the current price in KES, the old price crossed out, and a wishlist heart", "Add to Cart on every card, a cart counter in the header and a search button", "A floating WhatsApp chat button that follows the customer down the page"],
     ["Find boots, jerseys or training gear in a tap", "Spot sale prices and the saving instantly", "Save favourites and add items to the cart", "Ask the shop a question without leaving the page"],
     "work-maggies-collection.html", "Maggie\u2019s Collection", "Web design and development")

# ------------------------------ GALLERY -----------------------------------
GALLERY = [
 ("Projects", "Maggie\u2019s Collection homepage", "wide"), ("Team", "Creative portrait", "tall"), ("Events", "Client kickoff", ""),
 ("Projects", "Baari Sports Centre site", ""), ("Projects", "Mobile layouts", ""), ("Events", "Launch day", "wide"),
 ("Team", "Sprint planning", ""), ("Projects", "Systems and operations", "tall"), ("Events", "Community meetup", ""),
 ("Team", "On location", "wide"), ("Projects", "Campaign creatives", ""), ("Events", "Workshop", ""),
]
cats = ["Projects", "Team", "Events"]
chips = f'<button class="chip" data-filter="All" aria-pressed="true">All<small>{len(GALLERY)}</small></button>' + "".join(
    f'<button class="chip" data-filter="{c}" aria-pressed="false">{c}<small>{sum(1 for g in GALLERY if g[0]==c)}</small></button>' for c in cats)
tiles = ""
for i, (cat, title, size) in enumerate(GALLERY, 1):
    src = f"assets/gallery/{i:02d}.jpg"
    tiles += f'''<button class="tile {size}" data-cat="{cat}" data-title="{title}" data-full="{src}" aria-label="Open photo: {title}">
<div class="ph-art" data-t="{title}"></div><img src="{src}" alt="{title}" loading="lazy" onerror="this.remove()"><span class="tile-cap">{title}<small>{cat}</small></span></button>'''
gallery_body = f'''
<section class="phero"><div class="wrap"><h1>Gallery</h1><p class="lead">Projects, the people behind them and the moments in between.</p></div></section>
<section class="sec" style="padding-top:1rem"><div class="wrap">
  <div class="chips-row" role="group" aria-label="Filter photos">{chips}</div>
  <p class="vh" id="gal-live" aria-live="polite"></p>
  <div class="gal">{tiles}</div>
</div></section>
<dialog class="lb" aria-label="Photo viewer"><div class="lb-in">
  <div class="lb-top"><span></span><button class="icon-btn lb-close" aria-label="Close photo viewer">{ICON["x"]}</button></div>
  <div class="lb-stage"><button class="icon-btn lb-nav prev" aria-label="Previous photo">{ICON["prev"]}</button><div class="lb-stage-content"></div><button class="icon-btn lb-nav next" aria-label="Next photo">{ICON["next"]}</button></div>
  <div class="lb-cap" aria-live="polite"></div>
</div></dialog>
{cta("Want to see your project here?", "Start a project with us and we will show your work the way it deserves.")}
'''
page("gallery.html", "Gallery | Flynn Technologies",
     "Photos of Flynn Technologies projects, team and events.", gallery_body, "gallery.html")

# ------------------------------ ABOUT -------------------------------------
about_body = f'''
<section class="phero"><div class="wrap"><h1>Built by people who like making things work.</h1>
  <p class="lead">Flynn Technologies builds custom software, automates repetitive work and runs the digital marketing that grows your business.</p></div></section>
<section class="sec" style="padding-top:1rem" aria-labelledby="founder-h"><div class="wrap about-grid">
  <figure class="portrait" style="margin:0"><div class="initials" aria-hidden="true">JG</div><img src="assets/img/joseph-gitonga.jpg" alt="Joseph Gitonga, Founder and Director of Flynn Technologies" onerror="this.remove()"><figcaption><strong>Joseph Gitonga</strong><span>Founder and Director</span></figcaption></figure>
  <div><h2 id="founder-h">Why Flynn exists</h2>
    <div class="measure" style="margin-top:1.4rem"><p class="lead" style="color:var(--paper)">Joseph Gitonga founded Flynn Technologies to give businesses one dependable team for the technology and the marketing.</p>
    <!-- EDIT: replace with Joseph's own story: where he started, what he has built, why he started Flynn. -->
    <p class="mute" style="margin-top:1rem">Too many businesses end up with a good website nobody visits, or good marketing that sends people to a site that does not work. Flynn builds the two together so each makes the other better.</p>
    <p class="mute" style="margin-top:1rem">We build for the way customers really shop in Kenya: on a phone, on mobile data, and and with mobile payments such as M-Pesa. That shapes every page, every form and every button we make.</p></div>
    <div class="hero-cta"><a class="btn btn-primary" href="contact.html">Work with us</a><a class="btn btn-ghost" href="work.html">See our work</a></div></div>
</div></section>

<section class="sec sec--alt" aria-labelledby="mv-h"><div class="wrap">
  <div class="sec-head"><h2 id="mv-h">What we are working towards</h2></div>
  <div class="together">
    <article><h3>Our mission</h3><p class="mute">Build technology that works, and use it to help our clients grow.</p></article>
    <article><h3>Our approach</h3><p class="mute">Plain language, written plans and regular updates. You always know what is happening and why.</p></article>
    <article><h3>Our promise</h3><p class="mute">We only recommend what your business needs, including telling you when something is not worth building.</p></article>
  </div>
</div></section>

<section class="sec sec--light" aria-labelledby="val-h"><div class="wrap">
  <div class="sec-head"><h2 id="val-h">How we work</h2></div>
  <ul class="values">
    <li><h3>Ship things that work</h3><p>We test on real phones and real connections before anything goes live.</p></li>
    <li><h3>Be honest about time and cost</h3><p>You get a written scope and price first. If something changes, we tell you early.</p></li>
    <li><h3>Measure what matters</h3><p>We track the results that affect your business, not numbers that only look good.</p></li>
    <li><h3>Stay after launch</h3><p>A launch is the start. We keep improving, fixing and promoting.</p></li>
  </ul>
</div></section>

<section class="sec" aria-labelledby="wk-h"><div class="wrap">
  <div class="sec-head"><h2 id="wk-h">Working with us</h2><p class="lead">What to expect from the first message to launch day and beyond.</p></div>
  <ol class="next3">
    <li><h3>One point of contact</h3><p class="mute">You talk to the same person throughout, mostly on WhatsApp, with calls when they help.</p></li>
    <li><h3>Progress you can see</h3><p class="mute">You review the work at each stage and approve it before we move on.</p></li>
    <li><h3>You own your work</h3><p class="mute">Your domain, content and website are yours, and we hand everything over when we finish.</p></li>
  </ol>
</div></section>
{cta("Let\u2019s talk about your business.", "Send a message. Joseph or a member of the team will reply within one working day.")}
'''
page("about.html", "About | Flynn Technologies",
     "Flynn Technologies was founded by Joseph Gitonga to give businesses one team for custom software, AI automation and digital marketing.",
     about_body, "about.html")

# ------------------------------ CONTACT -----------------------------------
contact_body = f'''
<section class="phero"><div class="wrap"><h1>Let&rsquo;s build something.</h1>
  <p class="lead">Tell us about your project. We reply within one working day.</p></div></section>
<section class="sec" style="padding-top:1rem"><div class="wrap contact-grid">
  <div>
    <h2 style="font-size:1.6rem">Talk to us directly</h2>
    <div class="channels">
      <a class="channel" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}<span><small>WhatsApp, fastest reply</small>{C["phone_display"]}</span></a>
      <a class="channel" href="mailto:{C["email"]}">{ICON["mail"]}<span><small>Email</small>{C["email"]}</span></a>
      <a class="channel" href="tel:+{C["phone_intl"]}">{ICON["phone"]}<span><small>Call</small>{C["phone_display"]}</span></a>
      <div class="channel">{ICON["pin"]}<span><small>Based in</small>{C["location"]}</span></div>
    </div>
  </div>
  <form class="form" id="contact-form" action="{C["form_endpoint"]}" method="post" data-mailto="{C["email"]}" data-wa="{C["phone_intl"]}" novalidate>
    <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required><span class="err" role="alert"></span></div>
    <div class="field"><label for="f-company">Company name <span class="mute">(optional)</span></label><input id="f-company" name="companyname" type="text" autocomplete="organization"></div>
    <div class="field"><label for="f-email">Email address</label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="err" role="alert"></span></div>
    <div class="field"><label for="f-service">What do you need?</label><select id="f-service" name="service">
      <option>Custom software</option><option>AI and automation</option><option>Marketing and growth</option><option>Complete solution</option><option selected>Not sure yet</option></select></div>
    <div class="field two"><div class="field"><label for="f-time">When do you need it? <span class="mute">(optional)</span></label><select id="f-time" name="timeline"><option value="">Choose</option><option>As soon as possible</option><option>Within a month</option><option>In 1 to 3 months</option><option>Just exploring</option></select></div>
      <div class="field"><label for="f-budget">Budget range <span class="mute">(optional)</span></label><select id="f-budget" name="budget"><option value="">Choose</option><option>Under KES 50,000</option><option>KES 50,000 to 150,000</option><option>KES 150,000 to 500,000</option><option>Above KES 500,000</option><option>Not sure yet</option></select></div></div>
    <div class="field"><label for="f-msg">About your project</label><textarea id="f-msg" name="message" required></textarea><span class="err" role="alert"></span></div>
    <input class="hp" type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div class="form-actions"><button class="btn btn-primary" type="submit">Send message</button><button class="btn btn-ghost" type="button" id="wa-send">Send on WhatsApp instead</button></div>
    <div class="form-ok" tabindex="-1" role="status"><strong>Message ready.</strong> Thank you. We will reply within one working day. If your email app opened, press send there to finish.</div>
    <p class="form-note">We only use your details to reply to your enquiry.</p>
  </form>
</div></section>
<section class="sec sec--alt" aria-labelledby="nx-h"><div class="wrap">
  <div class="sec-head"><h2 id="nx-h">What happens next</h2></div>
  <ol class="next3">
    <li><h3>We reply</h3><p class="mute">Within one working day, usually sooner on WhatsApp.</p></li>
    <li><h3>We talk it through</h3><p class="mute">A short call or chat to understand your business, customers and goals.</p></li>
    <li><h3>You get a plan and a quote</h3><p class="mute">A written scope, timeline and price. No pressure, and no work starts until you agree.</p></li>
  </ol>
  <p class="mute" style="margin-top:1.8rem">We work with businesses across Kenya, and remotely from anywhere.</p>
</div></section>
'''
page("contact.html", "Contact | Flynn Technologies",
     "Start a project with Flynn Technologies. Message us on WhatsApp, email, or use the contact form.", contact_body, "contact.html")

# ------------------------------ LEGAL -------------------------------------
privacy_body = f'''
<section class="phero"><div class="wrap"><h1>Privacy policy</h1><p class="lead">How Flynn Technologies handles your information. Last updated October 2026.</p></div></section>
<section class="sec" style="padding-top:1rem"><div class="wrap prose">
<h2>Who we are</h2><p>Flynn Technologies is a software engineering and digital marketing company in Kenya, led by Joseph Gitonga. You can reach us at <a class="link" href="mailto:{C["email"]}">{C["email"]}</a>.</p>
<h2>What we collect</h2><ul><li>Details you send us through the contact form, email or WhatsApp: your name, company, email address, phone number, project details and budget range.</li><li>Basic visit information such as pages viewed and device type, if analytics is switched on for this site.</li></ul>
<h2>How we use it</h2><ul><li>To reply to your enquiry and prepare a quote.</li><li>To deliver the work you ask us to do.</li><li>To improve this website.</li></ul>
<p>We do not sell your personal information.</p>
<h2>Who we share it with</h2><p>We use trusted services to run this site, such as website hosting, a form service that delivers contact messages to us, and WhatsApp when you choose to message us. These providers process information only to provide their service.</p>
<h2>How long we keep it</h2><p>We keep enquiry details for as long as needed to respond and to work with you, then delete them when they are no longer required.</p>
<h2>Your rights</h2><p>Under the Kenya Data Protection Act, 2019, you can ask to see, correct or delete the personal information we hold about you. Email us and we will respond. You may also contact the Office of the Data Protection Commissioner.</p>
<h2>Changes</h2><p>We may update this policy and will change the date above when we do.</p>
</div></section>
'''
page("privacy.html", "Privacy policy | Flynn Technologies", "How Flynn Technologies collects, uses and protects your information.", privacy_body, "")

terms_body = f'''
<section class="phero"><div class="wrap"><h1>Terms of use</h1><p class="lead">The rules for using this website. Last updated October 2026.</p></div></section>
<section class="sec" style="padding-top:1rem"><div class="wrap prose">
<h2>Using this site</h2><p>This website describes the services of Flynn Technologies. By using it you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Our content</h2><p>The text, designs, logos and code on this site belong to Flynn Technologies or its clients and may not be copied or reused without permission. Project screenshots belong to the respective clients.</p>
<h2>Information on this site</h2><p>We work to keep the information accurate, but it is provided for general guidance. Descriptions of services are not a contract. Prices, timelines and deliverables are agreed in a written quote for each project.</p>
<h2>Quotes and projects</h2><p>Work begins only after you accept a written quote. Each project has its own scope, schedule and payment terms, which apply instead of anything general on this site.</p>
<h2>Links to other sites</h2><p>This site links to client websites and social platforms. We are not responsible for the content or practices of other websites.</p>
<h2>Liability</h2><p>To the extent the law allows, Flynn Technologies is not liable for losses that result from using this website.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of Kenya.</p>
<h2>Contact</h2><p>Questions about these terms: <a class="link" href="mailto:{C["email"]}">{C["email"]}</a>.</p>
</div></section>
'''
page("terms.html", "Terms of use | Flynn Technologies", "The terms for using the Flynn Technologies website.", terms_body, "")

# ------------------------------ 404 ---------------------------------------
page("404.html", "Page not found | Flynn Technologies", "This page does not exist.",
     '<section class="nf"><div class="wrap"><h1>404</h1><h2 style="margin-top:1rem">This page does not exist.</h2><p class="lead" style="margin:1rem auto 2rem">It may have moved, or the link may be wrong.</p><a class="btn btn-primary" href="index.html">Go to the homepage</a></div></section>',
     "")

# ------------------------------ SEO files ---------------------------------
today = datetime.date.today().isoformat()
urls = ["", "services.html", "work.html", "work-maggies-collection.html", "work-baari-sports-centre.html", "gallery.html", "about.html", "contact.html", "privacy.html", "terms.html"]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join(f"<url><loc>{C['domain']}/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {C['domain']}/sitemap.xml\n")
print("Built", len(urls) + 1, "pages")
