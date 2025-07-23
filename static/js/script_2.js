document.addEventListener("DOMContentLoaded", function () {
    console.log("Script loaded");
  
    const track = document.querySelector('.carousel-track');
    const leftBtn = document.querySelector('.left-nav');
    const rightBtn = document.querySelector('.right-nav');
    const card = document.querySelector('.carousel-card');
  
    console.log("track", track, "leftBtn", leftBtn, "rightBtn", rightBtn, "card", card);
  
    if (track && leftBtn && rightBtn && card) {
      console.log("Carousel script initialized");
  
      let currentSlide = 0;
  
      function getVisibleCards() {
        const width = window.innerWidth;
        if (width >= 992) return 4;
        if (width >= 768) return 3;
        if (width >= 576) return 2;
        return 1;
      }
  
      function updateCarousel(direction) {
        const totalCards = document.querySelectorAll('.carousel-card').length;
        const cardsVisible = getVisibleCards();
        const maxSlide = Math.ceil(totalCards / cardsVisible) - 1;
  
        if (direction === 'next') {
          currentSlide = Math.min(currentSlide + 1, maxSlide);
        } else if (direction === 'prev') {
          currentSlide = Math.max(currentSlide - 1, 0);
        }
  
        const shift = currentSlide * track.parentElement.offsetWidth;
        console.log(`Direction: ${direction}, Slide: ${currentSlide}, Shift: ${shift}`);
        track.style.transform = `translateX(-${shift}px)`;
      }
  
      leftBtn.addEventListener("click", () => updateCarousel("prev"));
      rightBtn.addEventListener("click", () => updateCarousel("next"));
  
      window.addEventListener("resize", () => {
        currentSlide = 0;
        track.style.transform = `translateX(0px)`;
      });
    }
  });
  