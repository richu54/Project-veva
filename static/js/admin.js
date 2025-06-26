
// manage user start --------------------------------------------------------------------------------------------------

// dashboard

document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
  
    if (toggleBtn && sidebar && mainContent) {
      toggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
        mainContent.classList.toggle('collapsed');
      });
    }
  });

// filter

  document.addEventListener('DOMContentLoaded', () => {
    const openBtn = document.getElementById('openFilterBtn');
    const closeBtn = document.getElementById('closeFilterBtn');
    const sidebar = document.getElementById('filterSidebar');
    const overlay = document.getElementById('filterOverlay');
  
    openBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      sidebar.classList.add('active');
      overlay.classList.add('active');
    });
  
    closeBtn?.addEventListener('click', () => {
      sidebar.classList.remove('active');
      overlay.classList.remove('active');
    });
  
    overlay?.addEventListener('click', () => {
      sidebar.classList.remove('active');
      overlay.classList.remove('active');
    });
  });

  // confirm delete

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.delete-btn2').forEach(function (btn) {
      btn.addEventListener('click', function (event) {
        event.preventDefault();
        const url = this.getAttribute('data-url');
  
        Swal.fire({
          title: 'Are you sure?',
          text: "This ID will be deleted permanently.",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#d33',
          cancelButtonColor: '#6c757d',
          confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = url;
          }
        });
      });
    });
  });
   

// manage user end ----------------------------------------------------------------------------------------------------

// add product start --------------------------------------------------------------------------------------------------

// update alert

document.addEventListener('DOMContentLoaded', function () {
  const notyf = new Notyf({
    duration: 3000,
    position: {
      x: 'right',
      y: 'bottom'
    }
  });

  const messages = document.querySelectorAll('.django-message');
  messages.forEach(msg => {
    const type = msg.getAttribute('data-type');
    const text = msg.textContent;

    if (type === 'success') {
      notyf.success(text);
    } else {
      notyf.error(text);
    }
  });
});

// add product end ----------------------------------------------------------------------------------------------------


// manage product start -----------------------------------------------------------------------------------------------

// clear products from search

const searchInput = document.querySelector('input[name="query"]');
  const searchForm = searchInput.closest('form');

  searchInput.addEventListener('input', function () {
    if (this.value === '') {
      searchForm.submit();  // Auto-submit when input is cleared
    }
  });
  
  // confirm delete

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.delete-btn').forEach(function (btn) {
      btn.addEventListener('click', function (event) {
        event.preventDefault();
        const url = this.getAttribute('data-url');
  
        Swal.fire({
          title: 'Are you sure?',
          text: "This product will be deleted permanently.",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#d33',
          cancelButtonColor: '#6c757d',
          confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = url;
          }
        });
      });
    });
  });

  // update alert

  document.addEventListener('DOMContentLoaded', function () {
    const notyf = new Notyf({
      duration: 3000,
      position: {
        x: 'right',
        y: 'bottom'
      }
    });
  
    const messages = document.querySelectorAll('.django-message-update');
    messages.forEach(msg => {
      const type = msg.getAttribute('data-type');
      const text = msg.textContent;
  
      if (type === 'success') {
        notyf.success(text);
      } else {
        notyf.error(text);
      }
    });
  });

// manage Product end -------------------------------------------------------------------------------------------------

// Order tracking start -----------------------------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', function () {
  const container = document.getElementById('django-messages');
  if (container) {
    const messages = container.querySelectorAll('.django-message');
    messages.forEach(msg => {
      const text = msg.textContent.trim();
      const type = msg.dataset.type || 'success';

      const toast = document.createElement('div');
      toast.classList.add('notify-toast', type);
      toast.textContent = text;
      document.body.appendChild(toast);

      setTimeout(() => {
        toast.remove();
      }, 4000); // 4 seconds
    });
  }
});

// Order tracking end -------------------------------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', function () {
  const messageContainer = document.getElementById('django-messages');
  const notifyContainer = document.getElementById('notify-container');

  if (messageContainer) {
    const messages = messageContainer.querySelectorAll('.django-message');
    messages.forEach(function (msg) {
      const type = msg.dataset.type || 'info';
      const text = msg.textContent;
      showNotify(text, type);
    });
  }

  function showNotify(message, type) {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show shadow`;
    alert.role = 'alert';
    alert.innerHTML = `
      ${message}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    notifyContainer.appendChild(alert);

    setTimeout(() => {
      alert.classList.remove('show');
      alert.classList.add('hide');
      setTimeout(() => notifyContainer.removeChild(alert), 400);
    }, 4000);
  }
});