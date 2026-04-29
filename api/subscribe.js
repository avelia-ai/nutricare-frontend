export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const { email } = req.body;
  if (!email || !email.includes('@')) return res.status(400).json({ error: 'Email invalide' });
  try {
    // Email de notification interne
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + process.env.RESEND_API_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'Mirella <noreply@mirella-ai.fr>',
        to: [process.env.NOTIFY_EMAIL],
        subject: 'Nouvelle préinscription Early Bird',
        html: '<h2>Nouvel inscrit !</h2><p><strong>Email :</strong> ' + email + '</p><p><strong>Date :</strong> ' + new Date().toLocaleString('fr-FR') + '</p>'
      })
    });

    // Email de confirmation à l'utilisateur
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + process.env.RESEND_API_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'Mirella <noreply@mirella-ai.fr>',
        to: [email],
        subject: 'Votre place chez Mirella est réservée !',
        html: `<!DOCTYPE html>
<html lang="fr">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#FFF5F0;font-family:'DM Sans',Arial,sans-serif">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#FFF5F0;padding:40px 20px">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%">

        <!-- HEADER -->
        <tr><td style="background:linear-gradient(135deg,#FF6B6B,#FF9A3C);border-radius:16px 16px 0 0;padding:40px;text-align:center">
          <div style="font-family:Georgia,serif;font-size:28px;font-weight:700;color:white;margin-bottom:8px">● Mirella</div>
          <div style="font-size:13px;color:rgba(255,255,255,.75);letter-spacing:.08em;text-transform:uppercase">Coach santé & nutrition IA</div>
        </td></tr>

        <!-- BODY -->
        <tr><td style="background:white;padding:48px 40px">
          <h1 style="font-family:Georgia,serif;font-size:24px;font-weight:700;color:#2D2D2D;margin:0 0 16px">Votre place est réservée. 🎉</h1>
          <p style="font-size:15px;color:#666;line-height:1.7;margin:0 0 24px">Bienvenue dans la communauté Mirella. Vous faites partie des premiers à bénéficier de notre offre Early Bird — <strong style="color:#FF6B6B">50% de réduction à vie</strong>, sans engagement, sans carte bancaire.</p>

          <!-- OFFRE BOX -->
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#2D2D2D;border-radius:12px;margin:0 0 32px">
            <tr>
              <td style="padding:28px;text-align:center">
                <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:#FF6B6B;margin-bottom:8px">Votre offre Early Bird</div>
                <div style="font-family:Georgia,serif;font-size:48px;font-weight:700;color:#FF6B6B;line-height:1">-50%</div>
                <div style="font-size:13px;color:rgba(255,255,255,.5);margin-top:8px">à vie · sans engagement · annulable à tout moment</div>
              </td>
            </tr>
          </table>

          <p style="font-size:15px;color:#666;line-height:1.7;margin:0 0 16px">Mirella sera disponible très prochainement. Vous serez parmi les premiers informés du lancement et votre réduction sera automatiquement appliquée à votre compte.</p>

          <p style="font-size:15px;color:#666;line-height:1.7;margin:0 0 32px">En attendant, voici ce qui vous attend :</p>

          <!-- FEATURES -->
          <table width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 32px">
            <tr>
              <td style="padding:12px 16px;background:#FFF5F0;border-radius:8px;margin-bottom:8px;display:block">
                <span style="color:#FF6B6B;font-weight:700">✓</span> <strong>Chat IA Nutritionnel</strong> — Votre coach disponible 24h/24, adapté à vos pathologies
              </td>
            </tr>
            <tr><td style="height:8px"></td></tr>
            <tr>
              <td style="padding:12px 16px;background:#FFF5F0;border-radius:8px">
                <span style="color:#FF6B6B;font-weight:700">✓</span> <strong>Menus hebdomadaires IA</strong> — 7 jours de repas générés selon votre profil
              </td>
            </tr>
            <tr><td style="height:8px"></td></tr>
            <tr>
              <td style="padding:12px 16px;background:#FFF5F0;border-radius:8px">
                <span style="color:#FF6B6B;font-weight:700">✓</span> <strong>Bilan sanguin IA</strong> — Résultats expliqués simplement avec conseils nutritionnels
              </td>
            </tr>
            <tr><td style="height:8px"></td></tr>
            <tr>
              <td style="padding:12px 16px;background:#FFF5F0;border-radius:8px">
                <span style="color:#FF6B6B;font-weight:700">✓</span> <strong>Détection visuelle IA</strong> — Analysez peau, yeux et ongles pour détecter des carences
              </td>
            </tr>
            <tr><td style="height:8px"></td></tr>
            <tr>
              <td style="padding:12px 16px;background:#FFF5F0;border-radius:8px">
                <span style="color:#FF6B6B;font-weight:700">✓</span> <strong>Et 10+ autres fonctionnalités</strong> — Simulateur, Oracle Santé, Passeport Santé...
              </td>
            </tr>
          </table>

          <p style="font-size:14px;color:#999;line-height:1.7;margin:0">Des questions ? Répondez simplement à cet email — nous sommes là pour vous.</p>
        </td></tr>

        <!-- FOOTER -->
        <tr><td style="background:#2D2D2D;border-radius:0 0 16px 16px;padding:28px 40px;text-align:center">
          <div style="font-size:13px;color:rgba(255,255,255,.4);line-height:1.7">
            © 2026 Mirella · Coach santé & nutrition IA<br>
            <a href="https://mirella-ai.fr/legal" style="color:#FF6B6B;text-decoration:none">Mentions légales</a> · 
            <a href="https://mirella-ai.fr" style="color:#FF6B6B;text-decoration:none">mirella-ai.fr</a>
          </div>
        </td></tr>

      </table>
    </td></tr>
  </table>
</body>
</html>`
      })
    });

    return res.status(200).json({ success: true });
  } catch(e) {
    return res.status(500).json({ error: 'Erreur' });
  }
}
