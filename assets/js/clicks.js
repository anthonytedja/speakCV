// https://css-tricks.com/snippets/jquery/smooth-scrolling/

// Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 0, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });

$('#profile-picture').click(function(){
    window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
  });

$('#codeblock-icon-email').click(function(){
    window.location.href = "mailto:anthony.tedja@mail.utoronto.ca";
  });

$('#codeblock-icon-github').click(function(){
    window.location.href = "https://github.com/anthonytedja";
  });

$('#codeblock-icon-linkedin').click(function(){
    window.location.href = "https://www.linkedin.com/in/anthonytedja";
  });

$('#codeblock-icon-devpost').click(function(){
    window.location.href = "https://devpost.com/anthonytedja";
  });

$('#codeblock-icon-unsplash').click(function(){
    window.location.href = "https://unsplash.com/@anthonytedja";
  });

$('#codeblock-icon-instagram').click(function(){
    window.location.href = "https://www.instagram.com/anthonytedja";
  });