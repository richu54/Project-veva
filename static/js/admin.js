
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
   

// manage user end ----------------------------------------------------------------------------------------------------
