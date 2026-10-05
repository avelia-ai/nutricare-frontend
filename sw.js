self.addEventListener('push', function(event) {
  var data = {};
  try { data = event.data.json(); } catch(e) {}
  event.waitUntil(
    self.registration.showNotification(data.title || 'Mirella', {
      body: data.body || '',
      icon: data.icon || '/images/mirella-icon.png',
      badge: '/images/mirella-icon.png',
      data: { url: data.url || '/app' }
    })
  );
});

self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  event.waitUntil(
    clients.openWindow(event.notification.data.url || '/app')
  );
});
