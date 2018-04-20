var card=$(".card")
var carousel=$(".container-fluid")
var button=$(".wrapper")
var bubble=$(".text_bubble")
var about_the_city=(".about_the_city")
// $(document).ready(function(){

//     var socket=io.connect('https://magic-city.herokuapp.com/');

//         socket.on('connect', function(){
//              console.log("mark mark");

//     });
//         socket.on('message', function(msg){
//              $("#messages").append("<li>"+msg+"</li>");
//              console.log($("#yoyo").val());
//              $("#yoyo").text(msg[1]);
//              $("#meme").text(msg[0]);

           
//     });
//         $("#sendbutton").on("click", function(){
//             socket.send($("#myMessage").val());
//             $("#myMessage").val("");
                               
//           });
    
//  });



$(document).ready(function(){
	$("#sendbutton").click(function(){
		var text=$("#myMessage").val();
		console.log(text);
		$.ajax({
			url: "/process",
			type: "POST",
			data: JSON.stringify(text),
			contentType: 'application/json; charset=utf-8',
			dataType: "json",
			success:function(resp){
				$("#yoyo").text(resp['reply'][1]);
				$("#meme").text(resp['reply'][0]);
			    $("#myMessage").val("")}
			
		});

	});
})


TweenMax.staggerFrom(card, 0.7, {y:100, opacity:0, delay:1}, 0.1);
TweenMax.from(carousel, 1, {y:100, opacity:0});
TweenMax.from(button, 1, {y:100, opacity:0});

TweenMax.staggerFrom(bubble, 2, {scale:0.5, opacity:0, delay:0.5, ease:Elastic.easeOut, force3D:true}, 0.2);


$("#sendbutton").click(function(){
  TweenMax.staggerFrom(bubble, 2, {scale:0.9, opacity:0, delay:0.2, ease:Elastic.easeOut, force3D:true}, 0.2);
});








