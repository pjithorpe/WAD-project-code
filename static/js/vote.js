$(document).ready(function() {
	
	if($('#doyouthink').is(':visible')) {
			$('#fact_count').hide();
			$('#fiction_count').hide();
		}
	
	$('#vote_fact').click(function(){
		var pageid;
		pageid = $(this).attr("data-pageid");
		$.get('/factorfiction/vote_fact/', {page_id: pageid}, function(data){
			$('#fact_count').html('</br>' + data + ' people have voted this as fact.');
			$('#fact_count').show();
			$('#fiction_count').show();
			$('#vote_fact').hide();
			$('#vote_fiction').hide();
			$('#page_or').hide();
			$('#doyouthink').hide();
		});
		window.location.href=window.location.href;
	});

	$('#vote_fiction').click(function(){
		var pageid;
		pageid = $(this).attr("data-pageid");
		$.get('/factorfiction/vote_fiction/', {page_id: pageid}, function(data){
			$('#fiction_count').html('</br>' + data + ' people have voted this as fiction.');
			$('#vote_fiction').hide();
			$('#vote_fact').hide();
			$('#page_or').hide();
			$('#doyouthink').hide();
		});
		window.location.href=window.location.href;
	});
		
});
