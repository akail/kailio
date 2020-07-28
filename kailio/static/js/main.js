$(window).scroll(function() {
    if($(this).scrollTop() > 300) {
        $('.navbar').removeClass('opaque');
    } else {
        $('.navbar').addClass('opaque');
    }
});
