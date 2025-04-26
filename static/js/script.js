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
      slideInterval = setInterval(() => {
          carousel.next();
      }, 5000);
  };
  
  const stopCarousel = () => {
      clearInterval(slideInterval);
  };
  
  startCarousel();
  
  $('#heroCarousel').hover(
      function() {
          stopCarousel();
      },
      function() {
          startCarousel();
      }
  );
  
  $(document).on('show.bs.modal', function () {
      stopCarousel();
  });
  
  $(document).on('hidden.bs.modal', function () {
      startCarousel();
  });
  
  $('#heroCarousel').on('slide.bs.carousel', function () {
      $('.carousel-caption').css('opacity', 0);
  });
  
  $('#heroCarousel').on('slid.bs.carousel', function () {
      $('.carousel-caption').css('opacity', 1);
      $('.hero-title, .hero-subtitle').css('animation', 'none');
      setTimeout(() => {
          $('.hero-title, .hero-subtitle').css('animation', 'fadeInUp 0.8s ease');
      }, 10);
  });
  
  function adjustCarouselHeight() {
      var windowHeight = $(window).height();
      var navHeight = $('nav').outerHeight() || 0;
      
      if ($(window).width() < 768) {
          $('.hero-carousel').css('height', (windowHeight - navHeight) + 'px');
      } else {
          $('.hero-carousel').css('height', '');
      }
  }
  
  adjustCarouselHeight();
  $(window).resize(adjustCarouselHeight);
  
  let touchStartX = 0;
  let touchEndX = 0;
  
  $('#heroCarousel').on('touchstart', function(e) {
      touchStartX = e.changedTouches[0].screenX;
  });
  
  $('#heroCarousel').on('touchend', function(e) {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
  });
  
  function handleSwipe() {
      if (touchEndX < touchStartX - 50) {
          carousel.next();
      }
      if (touchEndX > touchStartX + 50) {
          carousel.prev();
      }
  }
});