// Navigation bar start ------------------------------------------------------------------------------------

// catagory drop-down 

$(document).ready(function() {
    $("#categories-toggle").click(function() {
      $("#categories-dropdown").slideToggle(300); 
      $(".dropdown-icon").toggleClass("fa-chevron-down fa-chevron-up");
    });
  });

//   mobile view dropdown

$(document).ready(function(){
    $("#drop-down-mob-view").click(function(){
        $("#mob-view-drop").slideToggle();
    });
});

// Navigation bar end --------------------------------------------------------------------------------------

// Carousal start ------------------------------------------------------------------------------------------

const carouselEl = document.querySelector('#heroCarousel');
if (carouselEl) {
    const carousel = new bootstrap.Carousel(carouselEl, {
        interval: 5000,
        pause: "hover",
        wrap: true
    });

    let slideInterval;

    const startCarousel = () => {
        slideInterval = setInterval(() => carousel.next(), 5000);
    };

    const stopCarousel = () => clearInterval(slideInterval);

    startCarousel();

    $('#heroCarousel').hover(stopCarousel, startCarousel);
    $(document).on('show.bs.modal', stopCarousel).on('hidden.bs.modal', startCarousel);

    $('#heroCarousel')
      .on('slide.bs.carousel', () => $('.carousel-caption').css('opacity', 0))
      .on('slid.bs.carousel', () => {
        $('.carousel-caption').css('opacity', 1);
        $('.hero-title, .hero-subtitle').css('animation', 'none');
        setTimeout(() => $('.hero-title, .hero-subtitle').css('animation', 'fadeInUp 0.8s ease'), 10);
      });

    const adjustCarouselHeight = () => {
        const height = $(window).height() - ($('nav').outerHeight() || 0);
        $('.hero-carousel').css('height', $(window).width() < 768 ? height + 'px' : '');
    };

    adjustCarouselHeight();
    $(window).resize(adjustCarouselHeight);

    let touchStartX = 0;

    $('#heroCarousel').on('touchstart', e => touchStartX = e.changedTouches[0].screenX)
                     .on('touchend', e => {
                         const touchEndX = e.changedTouches[0].screenX;
                         if (touchEndX < touchStartX - 50) carousel.next();
                         if (touchEndX > touchStartX + 50) carousel.prev();
                     });
}

// Carousal end --------------------------------------------------------------------------------------------

// Category card start -------------------------------------------------------------------------------------


let lastScroll = window.scrollY;
const fadeElements = document.querySelectorAll('.fade-in');

function checkFade() {
  const currentScroll = window.scrollY;
  const scrollingDown = currentScroll > lastScroll;
  lastScroll = currentScroll;

  if (scrollingDown) {
    fadeElements.forEach(el => {
      if (el.classList.contains('visible')) return;
      
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.75) {
        el.classList.add('visible');
      }
    });
  }
}

checkFade();

let ticking = false;
window.addEventListener('scroll', () => {
  if (!ticking) {
    window.requestAnimationFrame(() => {
      checkFade();
      ticking = false;
    });
    ticking = true;
  }
});

// Category card end ---------------------------------------------------------------------------------------

// Signup start --------------------------------------------------------------------------------------------

// form validation

function validation() {
  let emailInput = document.getElementById('u_email');
  let passInput = document.getElementById('u_pass');
  let nameInput = document.getElementById('u_name');
  let mobileInput = document.getElementById('u_mobile');

  if (email(emailInput, 'Enter a valid email')) {
    if (pass(passInput, 'Passwords must be 6-8 characters long')) {
      if(names(nameInput)){
        if (mobile(mobileInput)){
          return true;
        }
      }
    }
  }

  return false;
}

function email(elem, msg) {
  let email_exp = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,4}$/;
  if (elem.value.match(email_exp)) {
    return true;
  } else {
    const notyf = new Notyf();
    notyf.error('Invalid Email');
    elem.focus();
    return false;
  }
}

function pass(elem, msg) {
  let password_exp = /^[a-zA-Z0-9]{6,8}$/;
  if (elem.value.match(password_exp)) {
    return true;
  } else {
    const notyf = new Notyf();
    notyf.error('Invalid Password');
    elem.focus();
    return false;
  }
}

function names(elem) {
  const name = elem.value.trim();
  
  if (name === "") {
    const notyf = new Notyf();
    notyf.error('Please enter your name');
    elem.focus();
    return false;
  }

  return true;
}

function mobile(elem,msg){
  let mobile_exp = /^[0-9]{10,13}$/;
  if(elem.value.match(mobile_exp)){
    return true
  }
  else {
    const notyf = new Notyf();
    notyf.error('Invalid mobile number');
    elem.focus();
    return false;
  }
}

// Signup OTP

window.addEventListener('DOMContentLoaded', () => {
  const otpContainer = document.getElementById('otp-container');
  if (otpContainer) {
      const otpBox = otpContainer.querySelector('.otp-box');

      setTimeout(() => {
          otpContainer.classList.remove('d-none');
          setTimeout(() => otpBox.classList.add('show'), 100);

          setTimeout(() => {
              otpBox.classList.remove('show');
              setTimeout(() => {
                  otpContainer.remove();
              }, 600);
          }, 7000);
      }, 2000);
  }
});

// Existing email error notification

document.addEventListener('DOMContentLoaded', function () {
  const errorDiv = document.getElementById('error-message');
  if (errorDiv) {
      const errorMessage = errorDiv.getAttribute('data-error');
      if (errorMessage) {
          const notyf = new Notyf(); 
          notyf.error(errorMessage);
      }
  }
});

// Signup successful alert

document.addEventListener('DOMContentLoaded', function () {
  const notyf = new Notyf();

  const successDiv = document.getElementById('signup-success');
  if (successDiv) {
      const successMessage = successDiv.getAttribute('data-success');
      if (successMessage) {
          notyf.success(successMessage);
      }
  }
});

// Invalid OTP alert

document.addEventListener('DOMContentLoaded', function () {
  const notyf = new Notyf();

  const errorDiv = document.getElementById('otp_error');
  if (errorDiv) {
      const errorMessage = errorDiv.getAttribute('data-error');
      if (errorMessage) {
          notyf.error(errorMessage);
      }
  }
});

// Signup end ----------------------------------------------------------------------------------------------

// Login start ---------------------------------------------------------------------------------------------


// login alert

document.addEventListener('DOMContentLoaded', function () {
  const notyf = new Notyf();

  const errorDiv = document.getElementById('login-error');
  if (errorDiv) {
      const errorMessage = errorDiv.getAttribute('data-error');
      if (errorMessage) {
          notyf.error(errorMessage);
      }
  }

  const successDiv = document.getElementById('login-success');
  if (successDiv) {
      const successMessage = successDiv.getAttribute('data-success');
      if (successMessage) {
          notyf.success(successMessage);
      }
  }
});

// Reset password email not valid

document.addEventListener('DOMContentLoaded', function () {
  const resetErrorDiv = document.getElementById('reset-error-message');
  if (resetErrorDiv) {
      const errorMessage = resetErrorDiv.getAttribute('data-error');
      if (errorMessage) {
          new Notyf().error(errorMessage);
      }
  }
});

// reset password OTP

window.addEventListener('DOMContentLoaded', () => {
  const otpContainer = document.getElementById('reset-otp-container');
  if (otpContainer) {
      const otpBox = otpContainer.querySelector('.reset-otp-box');

      setTimeout(() => {
          otpContainer.classList.remove('d-none');
          setTimeout(() => otpBox.classList.add('show'), 100);

          setTimeout(() => {
              otpBox.classList.remove('show');
              setTimeout(() => {
                  otpContainer.remove();
              }, 600);
          }, 7000);
      }, 2000);
  }
});

// reset OTP error

// 
document.addEventListener('DOMContentLoaded', function () {
  const errorDiv = document.getElementById('reset-error');
  if (errorDiv) {
      const errorMessage = errorDiv.getAttribute('data-error');
      if (errorMessage) {
          const notyf = new Notyf();
          notyf.error(errorMessage);
      }
  }
});

// Reset password successful

document.addEventListener('DOMContentLoaded', function () {
  const notyf = new Notyf();
  document.querySelectorAll('.alert.alert-success').forEach(function (alert) {
      const message = alert.textContent.trim();
      if (message) {
          notyf.success(message);
          alert.remove();
      }
  });
});

// product browsing start ----------------------------------------------------------------------------------


document.getElementById('sidebarToggle').addEventListener('click', () => {
  document.getElementById('sidebar').classList.toggle('collapsed');
});

const categorySections = document.querySelectorAll('.category-section');


document.querySelectorAll('[data-category]').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const category = link.getAttribute('data-category');
    
    categorySections.forEach(section => section.classList.add('d-none'));

    const target = document.getElementById(`section-${category}`);
    if (target) target.classList.remove('d-none');
  });
});

// category redirect

document.addEventListener("DOMContentLoaded", function () {
  const hash = window.location.hash;

  if (hash.startsWith("#section-")) {
      document.querySelectorAll(".category-section").forEach(section => {
          section.classList.add("d-none");
      });

      const target = document.querySelector(hash);
      if (target) {
          target.classList.remove("d-none");
      }
  }
});

//whishlist

function toggleWishlist(el) {
  const productId = el.getAttribute("data-product-id");
  const url = el.getAttribute("data-url");
  const notyf = new Notyf({ duration: 2000, position: { x: 'right', y: 'bottom' } });

  fetch(`${url}?product_id=${productId}`)
    .then(res => {
      if (res.status === 401) {
        notyf.error('Please login to use the wishlist.');
        return null;
      }
      return res.json();
    })
    .then(data => {
      if (!data) return;

      if (data.status === "added") {
        // show filled heart
        el.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="red"
               class="bi bi-heart-fill" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 
                  23.534 4.735 8 15-7.534 4.736 
                  3.562-3.248 8 1.314"/>
          </svg>`;
        notyf.success('Added to wishlist');
      } else if (data.status === "removed") {
        // show empty heart
        el.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor"
               class="bi bi-heart" viewBox="0 0 16 16">
            <path d="m8 2.748-.717-.737C5.6.281 
                     2.514.878 1.4 3.053c-.523 1.023-.641 
                     2.5.314 4.385.92 1.815 2.834 
                     3.989 6.286 6.357 3.452-2.368 
                     5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385
                     C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 
                     3.279-3.04 7.824 1.143q.09.083.176.171a3 
                     3 0 0 1 .176-.17C12.72-3.042 23.333 
                     4.867 8 15"/>`;
        notyf.error('Removed from wishlist');
      }
    })
    .catch(err => console.error(err));
}

// product refresh position

document.querySelectorAll("form").forEach(form => {
  form.addEventListener("submit", () => {
    localStorage.setItem("scrollPos", window.scrollY);
  });
});

window.addEventListener("load", () => {
  const scrollPos = localStorage.getItem("scrollPos");
  if (scrollPos) {
    window.scrollTo(0, parseInt(scrollPos));
    localStorage.removeItem("scrollPos");
  }
});

// clear products from search

$(document).ready(function () {
  const $searchInput = $('input[name="query"]');
  const $searchForm = $searchInput.closest('form');

  $searchInput.on('input', function () {
    if ($(this).val().trim() === '') {
      $searchForm.submit();  
    }
  });
});

// product browsing end ------------------------------------------------------------------------------------

// product detailes start ----------------------------------------------------------------------------------

//whishlist

function toggleWishlist_cart(el) {
  const svg = el.querySelector('svg');
  const isFilled = svg.classList.contains('bi-heart-fill');

  if (isFilled) {

    // unfilled heart

    el.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
           class="bi bi-heart mt-2 mb-5 text-danger" viewBox="0 0 16 16">
        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 
                 1.4 3.053c-.523 1.023-.641 2.5.314 
                 4.385.92 1.815 2.834 3.989 6.286 
                 6.357 3.452-2.368 5.365-4.542 
                 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 
                 10.4.28 8.717 2.01zM8 15C-7.333 4.868 
                 3.279-3.04 7.824 1.143q.09.083.176.171a3 
                 3 0 0 1 .176-.17C12.72-3.042 23.333 
                 4.867 8 15"/>
      </svg>
    `;
    
  } else {

    // red filled heart

    el.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="red"
           class="bi bi-heart-fill mt-2 mb-5" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 
                 23.534 4.735 8 15-7.534 4.736 
                 3.562-3.248 8 1.314"/>
      </svg>
    `;
  }
}

// product detailes end ------------------------------------------------------------------------------------

// cart page start -----------------------------------------------------------------------------------------

// next section

function gotoStep(step) {
  document.querySelectorAll('.cart-section').forEach(el => el.classList.remove('active'));
  document.querySelector('.section' + step).classList.add('active');

  document.querySelectorAll('.cart-step').forEach(el => el.classList.remove('active'));
  document.querySelector('.step' + step).classList.add('active');
}

// previous section
 
function gotoStep(step) {
  document.querySelectorAll('.cart-section').forEach(el => el.classList.remove('active'));
  document.querySelector('.section' + step).classList.add('active');

  document.querySelectorAll('.cart-step').forEach(el => el.classList.remove('active'));
  document.querySelector('.step' + step).classList.add('active');
}
