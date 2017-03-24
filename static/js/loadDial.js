// A script which draws the dial representing the 'vote swing'
// on a particular article.

document.addEventListener('DOMContentLoaded',buildDial,false);
	function buildDial() {
		
		// get the canvas element from the html template
		// also retrieving it's params.
		var canvas = document.getElementById('voteDialCanvas');
		var totalVotes = canvas.getAttribute('data-totalVotes');
		var fictions = canvas.getAttribute('data-fictions');
		var context = canvas.getContext('2d');
		
		// draw the outline semi circle
		context.beginPath();
		context.arc(125, 145, 100, 0, Math.PI, true);
		context.closePath();
		context.lineWidth = 8;
		context.strokeStyle = '#550000';
		context.stroke();
		
		// only fill in the circle if there are any votes
		if (totalVotes > 0) {
			
			// draw a blue semi circle to represent fact
			context.beginPath();
			context.moveTo(125, 145);
			context.arc(125, 145, 100, 0, Math.PI, true);
			context.closePath();
			context.fillStyle = 'blue';
			context.fill();
			
			// get the proportion of fiction votes compared with the total
			// and then turn this into the necessary angle for the red arc
			var innerAngle = -(Math.PI * (fictions/parseFloat(totalVotes)));
			
			// draw the red fiction vote arc
			context.beginPath();
			context.moveTo(125, 145);
			context.arc(125, 145, 100, 0, innerAngle, true);
			context.closePath();
			context.lineWidth = 1;
			context.fillStyle = 'red';
			context.fill();
			
			// use trig to find the co-ord of the intersection of the 2
			// arcs draw the dial needle
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