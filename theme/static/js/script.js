$( document ).ready(function() {
 	var pathname = window.location.pathname;
 	if (pathname != "/")
 	{
		$("#background").slideDown(); 		
 	}

});

$("#blog").on("click", function() {
	var pathname = window.location.pathname;
	if (pathname == "/") 
	{
		$("#background").slideDown();
		return false;
	}
});