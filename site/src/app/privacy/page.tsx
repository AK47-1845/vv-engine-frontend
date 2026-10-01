import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

export const metadata = { title: 'Privacy | Genuity Verify demonstration' };

export default function Privacy() {
  return <main id="main" className="container legal-page"><Link className="text-link" href="/"><ArrowLeft size={16} />Genuity Verify</Link><h1>Privacy, for this demonstration.</h1><p>This site does not send the contents of the pilot form to a server. The form generates a local JSON draft for you. No contact recipient is configured.</p><h2>Demonstration data</h2><p>Robot traces, failure events and report previews are synthetic. The interactive examples run in your browser and are not robot telemetry.</p><h2>Storage and requests</h2><p>No analytics or advertising service is included in this implementation. Hosting infrastructure may retain ordinary request logs under its own policies. Font files and product assets are served locally by the website.</p><h2>Before a public launch</h2><p>[REPLACE] The operator&apos;s legal identity, privacy contact, hosting details, retention policy and any pilot-submission processing must be finalized before collecting personal data.</p><p className="mono muted">IMPLEMENTATION NOTICE / 01 OCTOBER 2026 / NOT LEGAL ADVICE</p></main>;
}