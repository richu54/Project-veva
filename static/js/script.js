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



