
  (function(n,o,t,i,f) {
    n[i] = {}; var m = ['init', 'on']; n[i]._c = [];m.forEach(me => n[i][me] = function() {n[i]._c.push([me, arguments])});
    var elt = o.createElement(f); elt.type = "text/javascript"; elt.async = true; elt.src = t;
    var before = o.getElementsByTagName(f)[0]; before.parentNode.insertBefore(elt, before);
  })(window, document, 'https://embed.novu.co/embed.umd.min.js', 'novu', 'script');

  novu.init('Yon8kmtE4T-9', '#notification-bell', {
    subscriberId: "on-boarding-subscriber-id-123",
  });
  