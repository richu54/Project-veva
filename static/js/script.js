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
    $("#account-triggers").click(function() {
      $("#account-dropdowns").slideToggle(500); 
      $(".dropdown-icon2").toggleClass("fa-chevron-down fa-chevron-up");
    });
  });


//   mobile view dropdown

$(document).ready(function(){
    $("#drop-down-mob-view").click(function(){
        $("#drop-down-sm").slideToggle();
    })
})

// Navigation bar end --------------------------------------------------------------------------------------
