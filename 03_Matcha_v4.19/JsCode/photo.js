(function() {
	var video = document.getElementById('video'),
		canvas = document.getElementById('canvas'),
		context = canvas.getContext('2d'),
		sup0 = document.getElementById('supImage0'),
		sup1 = document.getElementById('supImage1'),
		photo = document.getElementById('photo'),
		vedorUrl = window.URL || window.webkitURL;

	navigator.getMedia = 	navigator.getUserMedia ||
							navigator.webkitGetUserMedia ||
							navigator.muzGetUserMedia ||
							navigator.msGetUserMedia;

	navigator.getMedia({
		video: true,
		audio: false
	}, function(stream) {
		video.srcObject = stream;
		video.play();
	}, function(error) {

	});

	document.getElementById('captureSubmit').addEventListener('click', function() {
		context.drawImage(video, (video.width * 1.575) - video.width, 0, video.width * 1.85, video.height * 1.5);
		var element = document.getElementById('photo'),
			img = canvas.toDataURL('image/jpeg');
		photo.setAttribute('src', img);
	})

	document.getElementById('filterAddSubmit0').addEventListener('click', function() {
		sup0.setAttribute('src', "./fltr/Star.png");
		context.drawImage(sup0, 10, 10, photo.width * .1, photo.height * .1);
		var element = document.getElementById('photo'),
			img = canvas.toDataURL('image/jpeg');
		photo.setAttribute('src', img);
	})

	document.getElementById('filterAddSubmit1').addEventListener('click', function() {
		sup1.setAttribute('src', "./fltr/Heart.png");
		context.drawImage(sup1, 10, 10, photo.width * .1, photo.height * .1);
		var element = document.getElementById('photo'),
			img = canvas.toDataURL('image/jpeg');
		photo.setAttribute('src', img);
	})

	document.getElementById('uploadSubmit').addEventListener('click', function() {
		var value = document.getElementById('photo').getAttribute("src");
		var xhttp = new XMLHttpRequest(); // AJAX to communicate js to php
		xhttp.open('POST', 'incs/imgUpload.inc.php', true);
		xhttp.setRequestHeader('Content-type', 'Application/x-www-form-urlencoded');
		xhttp.send('img='+encodeURIComponent(value));
	})

})();