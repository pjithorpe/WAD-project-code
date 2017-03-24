$(document).ready(function() {
	
	// Hides the fact and fiction counts if the
	//'Do you think this is F or F' prompt is visible
	if($('#doyouthink').is(':visible')) {
			$('#fact_count').hide();
			$('#fiction_count').hide();
		}
	
	// Listens for button click and then returns an html response displaying the fact vote count
	$('#vote_fact').click(function(){
		var pageid;
		pageid = $(this).attr("data-pageid");
		$.get('/factorfiction/vote_fact/', {page_id: pageid}, function(data){
			$('#fact_count').html('</br>' + data + ' people have voted this as fact.');
			// hide the used elements
			$('#vote_fact').hide();
			$('#vote_fiction').hide();
			$('#page_or').hide();
			$('#doyouthink').hide();
		});
		window.location.href=window.location.href;
	});

	// Listens for button click and then returns an html response displaying the fiction vote count
	$('#vote_fiction').click(function(){
		var pageid;
		pageid = $(this).attr("data-pageid");
		$.get('/factorfiction/vote_fiction/', {page_id: pageid}, function(data){
			$('#fiction_count').html('</br>' + data + ' people have voted this as fiction.');
			// hide the used elements
			$('#vote_fiction').hide();
			$('#vote_fact').hide();
			$('#page_or').hide();
			$('#doyouthink').hide();
		});
		window.location.href=window.location.href;
	});
		
});
