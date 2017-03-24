document.addEventListener('DOMContentLoaded',buildDial,false);
	function buildDial() {
		
		var canvas = document.getElementById('voteDialCanvas');
		var totalVotes = canvas.getAttribute('data-totalVotes');
		var fictions = canvas.getAttribute('data-fictions');
		var context = canvas.getContext('2d');
		
		context.beginPath();
		context.arc(125, 145, 100, 0, Math.PI, true);
		context.closePath();
		context.lineWidth = 8;
		context.strokeStyle = '#550000';
		context.stroke();
		
		if (totalVotes > 0) {
			context.beginPath();
			context.moveTo(125, 145);
			context.arc(125, 145, 100, 0, Math.PI, true);
			context.closePath();
			context.fillStyle = 'blue';
			context.fill();
			
			var innerAngle = -(Math.PI * (fictions/parseFloat(totalVotes)));
			
			context.beginPath();
			context.moveTo(125, 145);
			context.arc(125, 145, 100, 0, innerAngle, true);
			context.closePath();
			context.lineWidth = 1;
			context.fillStyle = 'red';
			context.fill();
			
			context.beginPath();
			context.moveTo(125, 145);
			if (innerAngle <= (Math.PI/2)){
				context.lineTo((125 + (75*Math.cos(innerAngle))) , (145 + (75 * Math.sin(innerAngle))));
			}
			else{
				context.lineTo((125 - (75*Math.cos(Math.PI - innerAngle))) , (145 - (75 * Math.sin(Math.PI - innerAngle))));
			}
			context.closePath();
			context.lineWidth = 8;
			context.strokeStyle = '#550000';
			context.stroke();
		}
		
		context.beginPath();
		context.moveTo(125, 145);
		context.arc(125, 145, 5, 0, Math.PI, true);
		context.closePath();
		context.lineWidth = 8;
		context.strokeStyle = '#550000';
		context.stroke();
			
	}