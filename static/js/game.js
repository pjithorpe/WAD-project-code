#var questions = [
#	["Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement", 
#	"News outlets around the world are reporting on the news that Pope Francis has made the unprecedented decision to endorse a US presidential candidate. His statement in support of Donald Trump was released from the Vatican this evening: 'I have been hesitant to offer any kind of support for either candidate in the US presidential election but I now feel that to not voice my concern would be a dereliction of my duty as the Holy See...",
#	"fake", 7, 15, '../../static/images/popetrump.jpg'],
#	["Trump Offering Free One-Way Tickets to Africa & Mexico for Those Who Wanna Leave America", 
#	"President elect Donald Trump has sensationally offered free one-way tickets to Mexico or Africa for anyone who wants to leave America in the aftermath of his election victory. The extraordinary, and highly controversial, offer was revealed by an aid at a press conference in New York this morning...",
#	"fake", 13, 17, '../../static/images/TrumpTickets.jpg'],
#	["Feral pig drinks 18 cans of beer, fights cow and then passes out drunk under tree", 
#	"The swine drank 18 beers on its bender in Port Hedland, Western Australia, according to ABC News. The alcohol also made the pig hungry and was seen looking through rubbish bags for something to eat...",
#	"true", 8, 19, '../../static/images/pig.jpg'],
#	["Cinnamon Roll Can Explodes Inside Man's Butt During Shoplifting Incident", 
#	"Las Vegas – Martin Klein, 41 of Las Vegas, was arrested after a shopping lifting incident turned horribly wrong. According to reports, Mr. Klein and his partner, Jerry Weis, had stolen several grocery items from the Las Vegas Walmart...",
#	"fake", 19, 7, '../../static/images/CinnamonRollMan.jpg'],
#	["Poll: 38% of Florida voters believe Ted Cruz could be the Zodiac Killer", 
#	"While a 62 percent majority of voters answered 'No' when asked if they believed Cruz was responsible for the string of murders in the early 70s, 10 percent answered 'Yes' and an additional 28 percent said they were unsure...",
#	"true", 11, 6, '../../static/images/FloridaPoll.jpg'],
#	["Hamster resurrection: Pet rises from the grave at Easter after being buried in garden", 
#	"Tink the hamster was found ‘cold and lifeless’ in the bottom of her cage and laid to rest by a couple who were looking after her for a friend. But the next day the rodent – who was not dead but hibernating – reappeared as perplexed Les Kilbourne-Smith crushed a pile of old boxes for recycling...",
#	"true", 15, 9, '../../static/images/hamster.jpg'],
#]

var questionCount = 0;
var correctAnswer = 0;


$(document).ready(function() {
		$("#answer").hide();
		$("#game_title").html(questions[questionCount][0]);
		$("#game_description").html(questions[questionCount][1]);
		$("#game_picture").attr('src', questions[questionCount][5]);
        $("#game_fact").click(function() {
			$("#game_picture").hide();
			$("#game_fact").prop('disabled', true);
			$("#game_fiction").prop('disabled', true);
			if(questions[questionCount][2] == "true"){
				$("#your_answer").html("Correct! This story is a Fact!");
				$("#current_answer_fact").html("Fact: " + (((questions[questionCount][3])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				$("#current_answer_fiction").html("Fiction: " + (((questions[questionCount][4])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				questions[questionCount][3] = questions[questionCount][3]+1;
				correctAnswer += 1;
			}
			else{
				$("#your_answer").html("Incorrect! This story is actually Fiction!");
				$("#current_answer_fact").html("Fact: " + (((questions[questionCount][3])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				$("#current_answer_fiction").html("Fiction: " + (((questions[questionCount][4])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				questions[questionCount][3] = questions[questionCount][3]+1
			}
			$("#answer").show();
        });
		$("#game_fiction").click(function() {
			$("#game_picture").hide();
			$("#game_fact").prop('disabled', true);
			$("#game_fiction").prop('disabled', true);
			if(questions[questionCount][2] == "fake"){
				$("#your_answer").html("Correct! This story is Fiction!");
				$("#current_answer_fact").html("Fact: " + (((questions[questionCount][3])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				$("#current_answer_fiction").html("Fiction: " + (((questions[questionCount][4])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				questions[questionCount][3] = questions[questionCount][4]+1
				correctAnswer += 1;
			}
			else{
				$("#your_answer").html("Incorrect! This story is actually a Fact!");
				$("#current_answer_fact").html("Fact: " + (((questions[questionCount][3])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				$("#current_answer_fiction").html("Fiction: " + (((questions[questionCount][4])/(questions[questionCount][3]+questions[questionCount][4]))*100).toFixed(2) + "%");
				questions[questionCount][3] = questions[questionCount][4]+1
			}
			$("#answer").show();
        });
		$("#game_next").click(function() {
			questionCount += 1;
			if(questionCount == questions.length){
				$("#your_answer").html("Thanks for playing!");
				$("#current_answer").html("You scored " + correctAnswer + " out of " + questions.length);
				$("#game_fact").hide();
				$("#game_fiction").hide();
				$("#game_title").hide();
				$("#game_description").hide();
				$("#game_next").hide();
				$("#current_answer_fact").hide();
				$("#current_answer_fiction").hide();
				$("#game_or").hide();
			}
			else{
			$("#game_picture").attr('src', questions[questionCount][5]);
			$("#answer").hide();
			$("#game_picture").show();
			$("#game_title").html(questions[questionCount][0]);
			$("#game_description").html(questions[questionCount][1]);
			$("#game_fact").prop('disabled', false);
			$("#game_fiction").prop('disabled', false);
			}
        });
      });
