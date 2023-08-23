<!DOCTYPE html>
<!-- This is an HTML document with a specified language -->
<html lang="en">
<head>
<meta charset="utf-8">
<!-- Define character encoding for the document -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<!-- Set compatibility mode for Internet Explorer -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Configure the viewport settings for responsive design -->
<title>Broken Authentication Login - Basic bruteforce example</title>
<!-- Set the title of the web page -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<!-- Include a stylesheet from a remote source (Bootstrap) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<!-- Include jQuery library from a remote source -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<!-- Include Bootstrap JavaScript library from a remote source -->
<style>
	/* Define inline CSS styles */
	.login-form {
		width: 340px;
    	margin: 50px auto;
	}
    .login-form form {
    	margin-bottom: 15px;
        background: #f7f7f7;
        box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
        padding: 30px;
    }
    .login-form h2 {
        margin: 0 0 15px;
    }
    .form-control, .btn {
        min-height: 38px;
        border-radius: 2px;
    }
    .btn {
        font-size: 15px;
        font-weight: bold;
    }
</style>
</head>
<body>
<!-- The main content of the web page starts here -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Broken Authentication Login - Basic bruteforce example</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<style>
	/* Define inline CSS styles */
	.login-form {
		width: 340px;
		margin: 50px auto;
	}
	.login-form form {
		margin-bottom: 15px;
		background: #f7f7f7;
		box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
		padding: 30px;
	}
	.login-form h2 {
		margin: 0 0 15px;
	}
	.form-control, .btn {
		min-height: 38px;
		border-radius: 2px;
	}
	.btn {
		font-size: 15px;
		font-weight: bold;
	}
</style>
</head>
<body>
<!-- Start of main content -->
<div class="login-form">
<?php
// Begin PHP code block
// Check if the server received a POST request with a 'userid' field
if (isset($_POST['userid'])) {
  // If the provided 'userid' is 'testuser' and 'passwd' is 'testpass'
	if (($_POST['userid'] === "testuser") && ($_POST['passwd'] === "testpass")) {
    // Display a success message
		echo '<div class="alert alert-primary"><strong>Welcome, testuser!</strong> </div>';
	} else {
    // Display an error message for invalid credentials
		echo '<div class="alert alert-warning"><strong>Invalid credential.</strong> </div>';
	}
}
?>
<!-- Display a login form -->
    <form action="" method="POST">
        <h2 class="text-center">Log in</h2>
        <div class="form-group">
          <!-- Input field for the username -->
            <input name="userid" type="text" class="form-control" placeholder="Username" required="required">
        </div>
        <div class="form-group">
          <!-- Input field for the password -->
            <input name="passwd" type="password" class="form-control" placeholder="Password" required="required">
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-block">Log in</button>
        </div>
    </form>
</div>

<!-- Display IP address -->
<div class="ip-address">
<?php
if (array_key_exists('HTTP_X_FORWARDED_FOR', $_SERVER)) {
	$realip = array_map('trim', explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']))[0];
} else if (array_key_exists('HTTP_CLIENT_IP', $_SERVER)) {
	$realip = array_map('trim', explode(',', $_SERVER['HTTP_CLIENT_IP']))[0];
} else if (array_key_exists('REMOTE_ADDR', $_SERVER)) {
	$realip = array_map('trim', explode(',', $_SERVER['REMOTE_ADDR']))[0];
} else {
	$realip = 'Unknown';
}

echo 'Your real IP address is: ' . htmlspecialchars($realip);
?>
</div>
<!-- End of the main content -->
</body>
</html>
