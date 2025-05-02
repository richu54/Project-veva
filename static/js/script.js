// Navigation bar start ------------------------------------------------------------------------------------

// catagory drop-down 

$(document).ready(function() {
    $("#categories-toggle").click(function() {
      $("#categories-dropdown").slideToggle(300); 
      $(".dropdown-icon").toggleClass("fa-chevron-down fa-chevron-up");
    });
  });

//   acount drop-down

$(document).ready(function() {
    $("#account-droptrigger").click(function() {
      $("#dropdown-account").slideToggle(500); 
      $(".dropdown-icon2").toggleClass("fa-chevron-down fa-chevron-up");
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

$(document).ready(function() {
  const carousel = new bootstrap.Carousel('#heroCarousel', {
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

  $('#heroCarousel').on('slide.bs.carousel', () => $('.carousel-caption').css('opacity', 0))
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
});

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

      // Delay OTP appearance (simulate "sending")
      setTimeout(() => {
          otpContainer.classList.remove('d-none');
          setTimeout(() => otpBox.classList.add('show'), 100);

          // Auto-dismiss after 7 seconds
          setTimeout(() => {
              otpBox.classList.remove('show');
              setTimeout(() => {
                  otpContainer.remove();
              }, 600);
          }, 7000);
      }, 2000); // 2-second delay
  }
});

// Existing email error notification

document.addEventListener('DOMContentLoaded', function () {
  const errorDiv = document.getElementById('error-message');
  if (errorDiv) {
      const errorMessage = errorDiv.getAttribute('data-error');
      if (errorMessage) {
          const notyf = new Notyf();  // Assuming Notyf is already loaded
          notyf.error(errorMessage);
      }
  }
});

// Signup successful alert

document.addEventListener('DOMContentLoaded', function () {
  const notyf = new Notyf();

  const errorDiv = document.getElementById('error-message');
  if (errorDiv) {
      const errorMessage = errorDiv.getAttribute('data-error');
      if (errorMessage) {
          notyf.error(errorMessage);
      }
  }

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

  const errorDiv = document.getElementById('error-message');
  if (errorDiv) {
      const errorMessage = errorDiv.getAttribute('data-error');
      if (errorMessage) {
          notyf.error(errorMessage);
      }
  }
});


// Signup end ----------------------------------------------------------------------------------------------


