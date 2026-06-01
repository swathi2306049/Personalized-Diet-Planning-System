document.addEventListener('DOMContentLoaded', function () {
  // Auto-hide alert messages after 4 seconds
  setTimeout(function () {
    document.querySelectorAll('.alert').forEach(function (el) {
      try { bootstrap.Alert.getOrCreateInstance(el).close(); }
      catch(e) {}
    });
  }, 4000);

  // Gym fields toggle on profile page
  var gymCheckbox = document.getElementById('gymFreak');
  var gymFields = document.getElementById('gymFields');
  if (gymCheckbox && gymFields) {
    gymFields.style.display = gymCheckbox.checked ? 'block' : 'none';
    gymCheckbox.addEventListener('change', function () {
      gymFields.style.display = this.checked ? 'block' : 'none';
    });
  }
});
