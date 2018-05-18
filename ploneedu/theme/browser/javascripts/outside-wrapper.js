function add_plone_links(){
    $("body").prepend('<div id="plonelinks"><a href="http://plone.org">Plone.org</a> | <a href="https://plone.com">Plone.com</a> | <a href="https://plone.org/download"> Download </a> | <a href="https://docs.plone.org/intro/index.html#what-is-plone" >What is Plone?</a> | <a href="https://community.plone.org/">Plone Support</a>  <img src="++resource++ploneedu.theme.images/ploneicon.png" alt="Plone Icon" /></div>');
}

$(document).ready(function() {
        if ($(window).width() > 618) {
            add_plone_links(); 
        }
        $(window).resize(function() {
            if ($(window).width() <= 618) { 
                   $('#plonelinks').remove();
            }
            if ($(window).width() > 618) {
                if ( $("#plonelinks").length == 0 ) {
                      add_plone_links();
                }
            }
         });
});
