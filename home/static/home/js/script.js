$(function(){
	$("nav#navigation ul li a").hover(function(){
		var newWidth = $(this).width() + 30;
		var newleft = $(this).position().left;
		
		$("span.line").stop().animate({
			width: newWidth,
			left: newleft
		}, 300);
		// alert ($(this).width());
		// alert ("Mouse Passando!!!");
	});
});