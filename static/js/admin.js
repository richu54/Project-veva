
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
