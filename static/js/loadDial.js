document.addEventListener('DOMContentLoaded',buildDial,false);
	function buildDial() {
		
		var canvas = document.getElementById('voteDialCanvas');
		var totalVotes = canvas.getAttribute('data-totalVotes');
		var fictions = canvas.getAttribute('data-fictions');
		var context = canvas.getContext('2d');
		
		context.beginPath();
		context.arc(125, 145, 100, 0, Math.PI, true);
		context.closePath();
		context.lineWidth = 5;
		context.fillStyle = 'blue';
		context.fill();
		context.strokeStyle = '#550000';
		context.stroke();
		
		var innerAngle = fictions/parseFloat(totalVotes);
		
		context.beginPath();
		context.moveTo(125, 145);
		context.arc(125, 145, 100, 0, -(Math.PI * innerAngle), true);
		context.closePath();
		context.lineWidth = 5;
		context.fillStyle = 'red';
		context.fill();
		context.strokeStyle = '#550000';
		context.stroke();
	}