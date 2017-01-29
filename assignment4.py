#assignment4.py
html>
	<head>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
	</head>
	<body>
		<div class= "jumbotron">
			<div class= "container">
				{% if forecast %}
					<h1>{{ forecast }}</h1>
					<a href="{{ url_for('assignment4') }}"> Look up another address </a>
				 {% else %}	
				 	<h1>Hello! Where do you live?</h1>
				 	<form action="/" class='form-inline'>
				 		<div class="form-group">
				 			<input type="text" name="address" placeholder="City, State" class="form-control">
				 		</div>	
				 		<input type="submit" value="Submit" class="btn btn-primary">
				 	</form>
				 {% endif %}
				<a href="{{ url_for('about') }}"> About this project </a>
			</div>
		</div>
	</body>
</html>