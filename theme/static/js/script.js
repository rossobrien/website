$( document ).ready(function() {
 	var pathname = window.location.pathname;
 	if (pathname != "/")
 	{
		$("#background").slideDown(); 		
 	}

});

$('.nav_box').on("click", function() {
	window.open($(this).find('a').attr('href'), "_self");
    return false;
});

$("#blog").on("click", function() {
	var pathname = window.location.pathname;
	if (pathname == "/") 
	{
		$("#background").slideDown();
		return false;
	}
});