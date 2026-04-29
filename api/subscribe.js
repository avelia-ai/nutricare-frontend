export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const { email } = req.body;
  if (!email || !email.includes('@')) return res.status(400).json({ error: 'Email invalide' });
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + process.env.RESEND_API_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from: 'Mirella <noreply@mirella-ai.fr>', to: [process.env.NOTIFY_EMAIL], subject: 'Nouvelle preInscription Early Bird', html: '<h2>Nouvel inscrit !</h2><p>Email : ' + email + '</p><p>Date : ' + new Date().toLocaleString('fr-FR') + '</p>' })
    });
    if (!r.ok) throw new Error('Resend error');
    return res.status(200).json({ success: true });
  } catch(e) {
    return res.status(500).json({ error: 'Erreur' });
  }
}
