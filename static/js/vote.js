$(document).ready(function() {
	$('#vote_fact').click(function(){
		var pageid;
		pageid = $(this).attr("data-pageid");
		$.get('/factorfiction/vote_fact/', {page_id: pageid}, function(data){
			$('#fact_count').html('</br>' + data + ' people have voted this as fact.');
			$('#vote_fact').hide();
			$('#vote_fiction').hide();
			$('#page_or').hide();
			$('#doyouthink').hide();
		});
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
	});
		
});