$("#nav ul li a[href^='#']").on('click', function(e) {

    // prevent default anchor click behavior
    e.preventDefault();
 
    // store hash
    var hash = this.hash;
 
    // animate
    $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 1000, function(){
 
        // when done, add hash to url
        // (default click behaviour)
        window.location.hash = hash;
      });
 
 });
 $(document).ready(function(){
  $('.page-item').click(function(){
   var selected=$(this);
   $('.page-item').removeClass('active');
   $(selected).addClass('active');
  });
  var $a=$('.a'),$b=$('.b'),$aboutvibhav=$('#aboutvibhav'),$aboutees=$('#aboutees');
  $a.click(function(){
    $aboutvibhav.fadeIn();
    $aboutees.fadeOut();
  })
  $b.click(function(){
    $aboutees.fadeIn();
    $aboutvibhav.fadeOut();
  })
})